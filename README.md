# Course Repository for EE 122/ME 141: Introduction to Control Systems at UC Merced

This repository contains all course materials for EE 122/ME 141: Introduction to Control Systems, including problem sets, solutions, lab assignments, and lecture notes.

## Structure
- `problem_sets/` contains all problem sets for each week. 
- `lecture_notes/` contains the lecture notes structured by each week.
- `macros.tex`: Macro file for course meta information (semester, year, instructor, etc.).
- `solutions/`: Private submodule for solutions (only accessible via CatCourses for UC Merced students).
- `labs/`: Private submodule for lab assignments and lab manuals (only accessible via CatCourses for UC Merced students).

## Students! Option 1: Getting Started through Overleaf

Click on the "Fork" on top-right of the main GitHub page of this repository to create a copy of this repository to your GitHub account. Then, on Overleaf home page, click on "New Project" and then on "Import from GitHub" to import this repository to Overleaf. Then, find the problem set or the lab manual that you would like to edit. You can edit any files on Overleaf that you'd like and simply click on "Recompile" to get the PDF file. 

To sync your Overleaf with the latest changes on GitHub, click on "Sync" button on GitHub on your fork page and then click on "Sync" on Overleaf.

## Students! Option 2: Getting Starting on your Computer

For this option, you must have a LaTeX compiler set up on your computer.

Start by cloning this repository 

```bash
git clone https://github.com/ee-ucmerced/ee122-control-systems.git
```

Then, edit any files you want on your local environment. To sync your local files with the GitHub updates, run `git pull`.

## License
This repository is for educational use in EE 122/ME 141 at UC Merced. See LICENSE file for more details.

## AI Use Statement
GitHub Copilot and GPT-5 are used in this repository at various places to generate plotting code and virtual manipulators using the Streamlit package. I have verified the technical accuracy but usual conditions apply: some things may be wrong / out of date. For the technical control systems content, I have been much more careful and I have verified the accuracy of all content. GitHub Copilot autocomplete is used for LaTeX, TikZ images, and other LaTeX settings but all of these have been carefully verified. Please create issues (and eventually, pull requests) to address any bugs that you find.

## Contact

All suggestions / contributions / comments are welcome. Please email these at ayushpandey at ucmerced dot edu or raise an issue on the repository.
