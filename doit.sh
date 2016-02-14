
function mainmenu
{
while :
do

  read -rsn1 -p ">" doit

  case "$doit" in
    [1-2])
      STATION=$doit
      curl http://localhost:8000/radio/$doit
      ;;

    s)
      curl http://localhost:8000/radio/stop
      ;;

    t)
      if [ ! -d "$STATION" ]; then
        curl http://localhost:8000/title/$STATION
      fi
      ;;

    q)
      curl http://localhost:8000/radio/stop
      printf "bye.\n"
      break
      ;;
    *)
      printf "(key: '$doit')"
      ;;

  esac
  sleep 0.1
done
}

mainmenu
