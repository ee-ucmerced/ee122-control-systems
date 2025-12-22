# EE122 Introduction to Control Systems LaTeX Project

This repository contains all course materials for EE122: Introduction to Control Systems, including problem sets, solutions, and lecture notes.

## Structure
- `homework/` contains the `hw1.tex`, and so on... along with the associated style files to work on the homework.
- `lecture_notes/` contains the lecture notes structured by each week.
- `macros.tex`: Macro file for course meta information (semester, year, instructor, etc.).
- `solutions/`: Submodule for solutions (only accessible via CatCourses for UC Merced students).

## Getting Started

To clone this repository with the solutions submodule (requires access to the private solutions repository):

```bash
git clone --recurse-submodules https://github.com/ee-ucmerced/ee122-control-systems.git
```

If you've already cloned the repository, initialize and update the submodule:

```bash
git submodule init
git submodule update
```

## License
This repository is for educational use in EE122 at UC Merced.

## AI Use Statement
GitHub Copilot and GPT-5 are used in this repository at various places to generate plotting code and virtual manipulators using the Streamlit package. I have verified the technical accuracy but usual conditions apply: some things may be wrong / out of date. For the technical control systems content, I have been much more careful and I have verified the accuracy of all content. GitHub Copilot autocomplete is used for LaTeX, TikZ images, and other LaTeX settings but all of these have been carefully verified. Please create issues (and eventually, pull requests) to address any bugs that you find.
