# Base in https://github.com/jackyzha0/quartz/pkgs/container/quartz
FROM ghcr.io/jackyzha0/quartz:sha-b34d521

# Copy content to show
COPY ./pkm/ ./content/

# Copy Quartz files
COPY ./quartz/quartz.config.ts ./quartz.config.ts
COPY ./quartz/quartz.layout.ts ./quartz.layout.ts
COPY ./quartz/lastmod.ts ./quartz/plugins/transformers/lastmod.ts
COPY ./quartz/index.ts ./quartz/components/index.ts
COPY ./quartz/Divider.tsx ./quartz/components/Divider.tsx
COPY ./quartz/custom.scss ./quartz/styles/custom.scss
