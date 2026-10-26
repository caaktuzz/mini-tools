# themes by caktuz / 1.0 / 26.10.2026

theme=0
theme_data=0
arg="$1"

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

  if [[ "$1" == "standart" ]]; then
      SETUP_THEME '\033[0m' '\033[0m'
  fi

  if [[ "$1" == "red" ]]; then
      SETUP_THEME '\033[31m' '\033[48;2;245;199;196m'
  fi

  if [[ "$1" == "green" ]]; then
      SETUP_THEME '\033[32m' '\033[48;2;217;245;196m'
  fi

  if [[ "$1" == "yellow" ]]; then
      SETUP_THEME '\033[33m' '\033[48;2;255;255;255m'
  fi

  if [[ "$1" == "blue" ]]; then
      SETUP_THEME '\033[34m' '\033[48;2;147;237;212m'
  fi


  if [[ -z $2 ]]; then :
  else
    if [[ $theme == "0" ]]; then
      echo "input error"
    else echo "theme is set!"
    fi
  fi
}

read_data_file

if [ -z "$arg" ]; then
   select_theme "$theme_data"
else
   theme_data="$arg"
   select_theme "$arg"
fi

sleep 0.5

blink() {
  while true; do
    select_theme "red"
    sleep 1
    select_theme "green"
    sleep 1
  done
}
#blink
