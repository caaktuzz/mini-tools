# themes by caktuz / 23.10.2026 


theme=0
theme_data=0
arg="$1"
echo "$arg"

path=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)/themes_data.txt
echo $path

read_data_file() {
  theme_data=$(< $path)
  echo "$theme_data"
}

write_data_file() {
  echo "$theme_data" > path
}

select_theme() {
  if [[ "$theme_data" == "standart" ]]; then
    echo -e "\033[0m"
    theme=1
    write_data_file
  fi

  if [[ "$theme_data" == "red" ]]; then
    echo -e "\033[0m"  # reset
    echo -e "\033[31m" # text
    echo -e "\033[48;2;245;199;196m" # background
    theme=1
    write_data_file
  fi

  if [[ "$theme_data" == "green" ]]; then
    echo -e "\033[0m" # reset
    echo -e "\033[32m" # text
    echo -e "\033[48;2;217;245;196m" # background
    theme=1
    write_data_file
  fi

  if [[ $theme == "0" ]]; then
    echo "input error"
  else echo "theme is set!"
  fi
}

read_data_file

if [ -z "$arg" ]; then
   select_theme "$theme_data"
else
   echo "arg is es"
   theme_data="$arg"
   select_theme "$arg"
fi

sleep 0.5

