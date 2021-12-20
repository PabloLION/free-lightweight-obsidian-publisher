## Example

See the public part of my note on [https://note.pablolion.com/](https://note.pablolion.com/).

## Usage

You don't have to download all this git.  
`deploy-obsidian.zsh` in the root folder does all the job.  
This is a one-file repo.

### Prerequisites

0. zsh
1. obsidian-export from [zoni/obsidian-export](https://github.com/zoni/obsidian-export)
2. mkdocs from [mkdocs.org](https://www.mkdocs.org/)
3. netlify-cli from [netlify.com](https://www.netlify.com/)

### Steps

1. Export these variables below in the .zshrc file or declare them in the `deploy-obsidian.zsh` file

   ```ZSH
   obsidian_mkdocs_root=?????? # root of mkdocs project contains the mkdocs.yml file
   obsidian_vault=?????? # root of the obsidian vault, contains the .obsidian folder
   reserved_folder_name=?????? # name of the folder that contains static non-exported resources, this folder in $obsidian_vault/docs won't be deleted by the script. This variable is default to `res`
   ```

2. Make sure that your mkdocs store markdown files in the `docs` folder, and the all static resources in `res` folder.
3. !! All files except `$reserved_folder_name` (`res` by default) in `$obsidian_mkdocs_root/docs` will be removed!!
4. Run `deploy-obsidian.zsh`, add it to your `.zshrc` file, etc. (If you don't have a netlify-cli, please answer "NO" to the first question.)
5. Enjoy.
6. (Optional) Write some feedback in this repo.

## FAQ

### Functionality

Q: Does it have the graph?
A: No, it doesn't.

### Trouble shooting

- `read -q invalid`: execute with zsh instead of with sh

## Bonus

### Switching from GitHub Wiki to this solution

- You can fix the GitHub flavor link with regex substitution/\[\[(.+)\|(.+)\]\]/g => [[$2|$1]] ([See it in my note](https://note.pablolion.com/coding/markdown%20note/#links-in-obsidian))

## Contributing

### Backup

#### Python attempt

- Discarded after 2 hours, because I find a easier way.
