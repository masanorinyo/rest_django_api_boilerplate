# This will link the app folder with pow server.
# This should be run once only
cd ./
echo 8000 > .port # Whatever port your app server is using
ln -s $PWD/.port ~/.pow/`basename $PWD`

