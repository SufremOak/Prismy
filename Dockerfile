FROM alpine AS stage

RUN apk add bazel \
    nodejs \
    python3 \
    gcc \
    make \
    ninja \
    golang

