var="hi there I'm the default."

while getopts u: flag
do
        case "${flag}" in
            u) var=${OPTARG};;
        esac
done
bash batch.sh "$var"
