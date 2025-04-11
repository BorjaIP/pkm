---
title:  Jenkins
created: Saturday 29th April 2023 17:05
Aliases: 
Tags: 
---

- [[Jenkins SSH Pipeline Steps]]
- [[Jenkins running multiple steps]]
- [[Jenkins pipeline Syntax]]
- [[How do I schedule jobs in Jenkins]]
- [[Continue Jenkins pipeline past failed stage]]
- [[Sequential stages within parallel pipeline in Jenkins]]
- [[How to run multiple stages on the same node with declarative Jenkins pipeline]]
# Scripts

```groovy
script {
    // Trigger by another webhook
    def upstreamCause = currentBuild.rawBuild.getCause(hudson.model.Cause$UpstreamCause)
    UPSTREAM = upstreamCause
    // Get build number from trigger webhook
	def upstreamBuild = Jenkins.instance.getItemByFullName(upstreamCause?.upstreamProject).getBuildByNumber(upstreamCause?.upstreamBuild)
    // Get environment action from trigger webhook
	def upstreamEnv = upstreamBuild.getAction(org.jenkinsci.plugins.workflow.cps.EnvActionImpl).getEnvironment()
	PARENT_ENV = upstreamEnv
    // Trigger by user
    def isStartedByUser = currentBuild.rawBuild.getCause(hudson.model.Cause$UserIdCause) != null
    // Get all Causes for the current build
    def causes = currentBuild.rawBuild.getCauses()
    println causes
}
```

- Select agent to run a Pipeline.

```bash
agent {label 'slave'}
```

- Select Node to run a Pipeline.

```bash
{
    node {
        label 'nodejs'
    }
}
```
# Variables

- [List of variabales](https://www.perforce.com/manuals/jenkins/Content/P4Jenkins/variable-expansion.html)

```groovy
# Only works on multibranch pipeline
env.BRANCH_NAME

# Workaround
\\...
stage('Test') {
        steps {
            script {
                branchName = sh(label: 'getBranchName', returnStdout: true, script: 'git rev-parse --abbrev-ref HEAD').trim()
                println branchName
            }   
        }
      } 
\\...
```