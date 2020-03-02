# Script to add file in GitHb

echo "Welcome to GitHub"

echo "Enter the file name to upload on GitHub"
read filename

echo "Adding filename..."
git add $filename

echo "Enter the upload description"
read desc
git commit -m "$desc"

git push origin master

echo "$filename added sucessfully!!"
