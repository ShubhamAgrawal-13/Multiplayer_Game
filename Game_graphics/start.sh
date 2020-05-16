trap "exit" INT TERM ERR
trap "kill 0" EXIT

python3 game_server.py &
sleep 3
python3 gamer.py shubham &
python3 gamer.py vedant &
python3 gamer.py richa &
python3 gamer.py ria &
python3 gamer.py shrayans &

wait
