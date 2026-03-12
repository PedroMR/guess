cd ~/p/guess
git restore game.html && echo "Restored game.html (version shenanigans)" 
git pull && echo "Pulled."

#COMMIT_HASH=$(git rev-parse HEAD)
COMMIT_HASH=$(git log --pretty="%h %ad" -1 game.html)

echo $COMMIT_HASH
if [ -n "$COMMIT_HASH" ]; then
    # Replace a placeholder string in your HTML file with the hash
    sed -i "s/%Version.*%/%Version $COMMIT_HASH%/" game.html
fi
