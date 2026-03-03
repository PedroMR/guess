COMMIT_HASH=$(git rev-parse HEAD)
git pull
# Replace a placeholder string in your HTML file with the hash
sed -i "s/GIT_VERSION/$COMMIT_HASH/" index.html