sudo /greengrass/v2/bin/greengrass-cli deployment create \
  --recipeDir /home/husam/src/gg2_components/recipes \
  --artifactDir /home/husam/src/gg2_components/artifacts \
  --merge "com.example.buttony=1.0.1"

sudo /greengrass/v2/bin/greengrass-cli deployment create \
  --recipeDir /home/husam/src/gg2_components/recipes \
  --artifactDir /home/husam/src/gg2_components/artifacts \
  --merge "com.example.lighty=1.0.0"

sudo /greengrass/v2/bin/greengrass-cli deployment create \
  --recipeDir /home/husam/src/gg2_components/recipes \
  --artifactDir /home/husam/src/gg2_components/artifacts \
  --merge "com.example.blinky=1.0.1"