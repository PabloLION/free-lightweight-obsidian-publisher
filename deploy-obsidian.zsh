#!/bin/zsh

#### requirements:
# 0. zsh
# 1. obsidian-export from zoni/obsidian-export
# 2. mkdocs from mkdocs.org
# 3. netlify-cli from netlify.com

#### Usage:
# export these variables below or write them here
# obsidian_mkdocs_root=??????      # root of mkdocs project contains the mkdocs.yml file
# obsidian_vault=??????            # root of the obsidian vault, contains the .obsidian folder
# reserved_folder_name=??????      # name of the folder that contains mkdocs static resources
#                                  # this folder in $obsidian_vault/docs won't be deleted by the script 

#### Trouble shooting:
# read -q invalid: execute with zsh instead of with sh

reserved_folder_name='res' #name of the folder that contains mkdocs static resources in $obsidian_vault/docs
if return_value=$(obsidian-export -v); then
  # printf 'obsidian-export -v succeded, the output was «%s»\n' "$return_value"
  if [[ -n "$obsidian_vault" ]] ; then
    # printf 'obsidian-vault succeded'
    :
  else
    read -p 'Enter obsidian vault path: ' obsidian_vault
  fi
  (cd "$obsidian_mkdocs_root/site" && rm -rf *)
  (cd "$obsidian_mkdocs_root/docs" && ls | grep -v ^"$reserved_folder_name"$ | xargs rm -rf)
  delete_failed=$(cd "$obsidian_mkdocs_root/docs" && ls | grep -v ^"$reserved_folder_name"$)
  if [[ -n "$delete_failed" ]] ; then
    printf 'Failed to delete these files:\n %s' "$delete_failed"
    read -q read_to_continue\?"Failed to delete files above. Press any key to continue..."
  fi
  $(obsidian-export "$obsidian_vault" "$obsidian_mkdocs_root/docs")
  
  ## deploy to netlify
  read -q deploy_to_netlify\?'Confirm deploy to netlify? (y/n [n])'
  echo ""
  if [[ "$deploy_to_netlify" == 'y' ]] ; then
    (cd "$obsidian_mkdocs_root/" && mkdocs build && ntl deploy --dir=site --prod)
  fi
  # (cd "$obsidian_mkdocs_root/" && mkdocs build && $(/usr/bin/open -a "/Applications/Google Chrome.app" 'http://127.0.0.1:8000/') && mkdocs serve)
  
  ## serve
  read -q local_serve\?'Serve locally? (y/n [n])'
  echo ""
  if [[ "$local_serve" == 'y' ]] ; then
    (cd "$obsidian_mkdocs_root/" && mkdocs serve)
    (/usr/bin/open -a "/Applications/Google Chrome.app" 'http://127.0.0.1:8000/')
  fi

else
  echo 'ERROR: deploy-obsidian didn''t run because obsidian-export is not a command'
fi