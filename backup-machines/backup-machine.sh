# 03.11.2026

FILES_PATH="arc_test.txt"
ARCHIVE_PATH="database_backup.zip"

ARG_1="$1"
ARG_2="$2"

BACKUP_FUNC() {
  zip -r "$FILES_PATH" "$ARCHIVE_PATH"
  echo "complete"
}
BACKUP_FUNC
