username=piet2
age=43
fullname="Pieter Vandenberge"

while getopts u:a:f: flag
do
        case "${flag}" in
            u) username=${OPTARG};;
            a) age=${OPTARG};;
            f) fullname=${OPTARG};;
        esac
done
echo "Username: $username";
echo "Age: $age";
echo "Full Name: $fullname";
