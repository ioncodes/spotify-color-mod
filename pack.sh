for D in `find . -type d`
do
    zip -r "${D}.spa" "${D}"
done
