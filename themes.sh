# themes by caktuz / 1.3 / 31.10.2026

theme=0
theme_data=0
ansi_code=""
arg="$1"

path=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)/themes_data.txt
if [[ ! -f $path ]] then
  echo "файл не найден"; sleep 1
  touch themes_data.txt
  echo "создан в локальной папке"
fi

echo $path

read_data_file() {
  IFS= read -r theme_data < $path
  echo "$theme_data"
}

write_data_file() { # saving configurations data
  echo "$theme_data" > "$path"
  echo "$ansi_code" >> "$path"
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
      SETUP_THEME '\033[0m' '\033[0m'; ansi_code="\033[0m"
  fi

  if [[ "$1" == "red" ]]; then
      SETUP_THEME '\033[31m' '\033[48;2;245;199;196m'; ansi_code='\033[31m \033[48;2;245;199;196m'
  fi

  if [[ "$1" == "green" ]]; then
      SETUP_THEME '\033[32m' '\033[48;2;217;245;196m'; ansi_code='\033[32m \033[48;2;217;245;196m'
  fi

  if [[ "$1" == "yellow" ]]; then
      SETUP_THEME '\033[33m' '\033[48;2;255;255;255m'; ansi_code='\033[33m \033[48;2;255;255;255m'
  fi

  if [[ "$1" == "blue" ]]; then
      SETUP_THEME '\033[34m' '\033[48;2;147;237;212m'; ansi_code='\033[34m \033[48;2;147;237;212m'
  fi

  if [[ "$1" == "purple" ]]; then
      SETUP_THEME '\033[35m' '\033[48;2;237;168;247m'; ansi_code='\033[35m \033[48;2;237;168;247m'
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

if [ -z "$arg" ]; then # if argument is not transferred - configuration using recorded data
   select_theme "$theme_data"
else
   theme_data="$arg"
   select_theme "$arg"
fi

sleep 0.5

echo $ansi_code
write_data_file

blink() { # tipa migalka temami. poka ploho rabotaet
  while true; do
    select_theme "red"
    sleep 1
    select_theme "green"
    sleep 1
  done
}
#blink
