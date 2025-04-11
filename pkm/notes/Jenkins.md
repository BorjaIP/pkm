---
title:  Jenkins
created: Saturday 29th April 2023 17:05
Aliases: 
Tags: 
---

- [SSH Pipeline Steps](https://github.com/jenkinsci/ssh-steps-plugin#configuration)
- [Running multiple steps](https://www.jenkins.io/doc/pipeline/tour/running-multiple-steps/#running-multiple-steps)
- [Pipeline Syntax](https://www.jenkins.io/doc/book/pipeline/syntax/)
- [Running multiple steps](https://www.jenkins.io/doc/pipeline/tour/running-multiple-steps/)
- [How do I schedule jobs in Jenkins?](https://stackoverflow.com/questions/12472645/how-do-i-schedule-jobs-in-jenkins)
- [Continue Jenkins pipeline past failed stage](https://stackoverflow.com/questions/40600621/continue-jenkins-pipeline-past-failed-stage)
- [Sequential stages within parallel pipeline in Jenkins](https://stackoverflow.com/questions/59688963/sequential-stages-within-parallel-pipeline-in-jenkins)
- [How to run multiple stages on the same node with declarative Jenkins pipeline?](https://stackoverflow.com/questions/44870978/how-to-run-multiple-stages-on-the-same-node-with-declarative-jenkins-pipeline)

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