echo "# TEST" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/RajneeshSrivastava/TEST.git
git remote -v
git push -u origin master

git help