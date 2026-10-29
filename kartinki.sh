# kartinki terminale restoration by caktuz / 1.0 / 26.10.2026

export SYSTEMD_PAGER=""
clear

general_color="\033[0m"

read_theme_data() {
  path=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)/themes_data.txt
  general_color=$(tail -n 1 $path)
}
read_theme_data

echo "hellow"
sleep 0.5
echo "KARTINKI TERMINALE"
sleep 0.3

echo -e "\033[32m                                           "
echo -e         "     __  __  _   _    __     __ __  __  __ "
echo -e         "    /_  /_|  /_/ / / /_/    /  / / /_/ /_/ "
echo -e         "   __/ /  | / / /_/ / \    /_ /_/ / \ /   $general_color"

echo ""
sleep 0.1

echo -e "$(hostnamectl)$general_color"
echo ""

sleep 0.1
echo -e "\033[36m$(dir --all)"
echo -e "$general_color"
