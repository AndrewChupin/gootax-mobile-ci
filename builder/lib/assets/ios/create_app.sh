#!/usr/bin/env bash

echo produce create \
-u "$APPLE_ID" \
-a "$BUNDLE" \
-q "$APP_NAME" \
-c "$ITUNES_TEAM_NAME" \
-z "$INIT_VERSION" \
-y "$SKU" \
-j "$PLATFORM" \
-m "$LANGUAGE" \
-l "$APPLE_TEAM_NAME" \
-p "$ITUNES_TEAM_NAME"

fastlane produce create \
-u "$APPLE_ID" \
-a "$BUNDLE" \
-q "$APP_NAME" \
-c "$ITUNES_TEAM_NAME" \
-z "$INIT_VERSION" \
-y "$SKU" \
-j "$PLATFORM" \
-m "$LANGUAGE" \
-l "$APPLE_TEAM_NAME" \
-p "$ITUNES_TEAM_NAME"
