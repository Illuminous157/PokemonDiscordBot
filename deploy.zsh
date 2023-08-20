#!/usr/bin/env zsh
# shellcheck disable=SC2164
cd ~/PycharmProjects/PokemonBot/
rm ../PokemonBot.zip
zip -r -o ../PokemonBot.zip ../PokemonBot -y
scp ../PokemonBot.zip andrew@20.51.221.90:~/PokemonBot.zip
ssh andrew@20.51.221.90 "sudo systemctl stop PokeBot.service"
ssh andrew@20.51.221.90 "sudo unzip ~/PokemonBot.zip"
ssh andrew@20.51.221.90 "sudo rm ~/PokemonBot.zip"
ssh andrew@20.51.221.90 "sudo rm -d -r /opt/PokemonBot"
ssh andrew@20.51.221.90 "sudo mv ~/PokemonBot /opt/PokemonBot"
ssh andrew@20.51.221.90 "sudo systemctl start PokeBot.service"


