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
  echo "$theme_data" > "$path"
}

select_theme() {
  SETUP_THEME() {
    echo -e "\033[0m" # reset
    echo -e "$1"      # text
    echo -e "$2"      # background
    theme=1
    write_data_file
  }

  if [[ "$theme_data" == "standart" ]]; then
      SETUP_THEME '\033[0m' '\033[0m'
  fi

  if [[ "$theme_data" == "red" ]]; then
      SETUP_THEME '\033[31m' '\033[48;2;245;199;196m'
  fi

  if [[ "$theme_data" == "green" ]]; then
      SETUP_THEME '\033[32m' '\033[48;2;217;245;196m'
  fi

  if [[ "$theme_data" == "yellow" ]]; then
      SETUP_THEME '\033[33m' '\033[48;2;255;255;255m'
  fi

  if [[ "$theme_data" == "blue" ]]; then
      SETUP_THEME '\033[34m'  '\033[48;2;147;237;212m'
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

