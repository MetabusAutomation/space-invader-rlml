**Quick‑Start Steps: RL on Space Invaders (PowerShell‑friendly)**

---

### 0 . Design Choices (fixed for v0)
- **Game**: `ALE/SpaceInvaders-v5` from `gymnasium[atari]`
- **Observations**: 4‑stacked 84 × 84 grayscale frames
- **Actions**: Minimal 6‑button set (NOOP, FIRE, LEFT, RIGHT, LEFTFIRE, RIGHTFIRE)
- **Reward**: Score delta per step (native)
- **Algorithm**: DQN (Stable‑Baselines3 default CNN)
- **Tracking**: TensorBoard

---

### 1 . Project Bootstrap & Environment Smoke Test
1. **Clone/Fork & `cd`** into the repo.
2. **Install Poetry** (one‑time per machine):
   ```powershell
   pipx install poetry    # or  pip install --user poetry
   ```
3. **Install Dependencies**: This installs exact versions from `poetry.lock`, including `gymnasium[atari]`, `pygame`, `autorom`, etc.
   ```powershell
   poetry install
   ```
4. **Select Python Interpreter (VS Code)**: Before running any Python code, ensure VS Code is using the interpreter from the Poetry environment. Open the Command Palette (`Ctrl+Shift+P`), run `Python: Select Interpreter`, and choose the one whose path contains `.venv` or the project name.
5. **Accept ROM License**: AutoROM needs license approval once per environment (run this in the terminal).
   ```powershell
   poetry run AutoROM --accept-license
   ```
6. **Verify Environment via Debugger**: This project includes a VS Code launch configuration (`.vscode/launch.json`) and a test script (`test_env.py`) to verify environment loading, rendering, and interaction.
   - Go to the "Run and Debug" view in VS Code (Ctrl+Shift+D).
   - Select `Python: test_env.py (Poetry)` from the dropdown.
   - Press the green play button (F5).
   - *Expected Outcome*: A game window should open. Test controls (Left/Right Arrows, Space) and confirm you see flickering alien bullets (due to `frameskip=1`).
   - *Alternative (Terminal)*: You can also run `poetry run python test_env.py`.
   - *Troubleshooting*: If it fails, ensure the correct Python interpreter is selected (Step 4), `poetry install` completed, and `AutoROM` ran successfully.
7. **(First Time Only) Initial Setup Details**:
   - If you were setting up this project *from scratch* (no `pyproject.toml`/`lock` file), the necessary packages were:
     ```powershell
     # poetry init # (if no pyproject.toml)
     poetry add gymnasium[atari] stable-baselines3 torch torchvision tensorboard opencv-python black ruff pygame autorom
     ```
   - The `test_env.py` script (included in the repo) was created to debug initial setup issues:
     ```python
     # test_env.py (Included in repository)
     import ale_py # noqa: F401
     _ = ale_py
     import gymnasium
     from gymnasium.utils.play import play
     import pygame
     # ... (rest of the script as previously defined) ...
     ```
8. **Add ROM Note**: Ensure `README.md` notes that Gymnasium/ALE-Py uses Atari ROMs, potentially distributed via AutoROM.
9. **Commit Often**: If you made local changes (e.g., tweaking `test_env.py`), commit them.

---

### 2 . Training Pipeline Skeleton *(no code yet)*
1. **Prompt Cursor** to create `train.py` that:
   - Builds the Atari env with proper wrappers.
   - Instantiates a DQN model.
   - Trains for a small number of steps first (e.g., 50 k) so you can iterate fast.
   - Includes *verbose* inline comments explaining *why* each wrapper / hyper‑param is used.
2. **Run the Training Script (Debugger Recommended)**:
   - **Option A (Debugger)**:
     1. Add a new configuration to `.vscode/launch.json` for `train.py` (copy the existing one and change `name` and `program`).
     2. Select the new configuration in the "Run and Debug" view and press F5.
   - **Option B (Terminal)**:
     ```powershell
     poetry run python train.py
     ```
3. Check that logs appear in `./tb/` and a model checkpoint saves.
4. Iterate: increase timesteps once basic loop works.

---

### 3 . Evaluation & Visualization Skeleton
1. **Prompt Cursor** to generate `evaluate.py` that:
   - Loads the saved checkpoint.
   - Runs 10 episodes and prints mean score.
   - Optionally records frames and writes a GIF—include comments on each step.
2. **Execute Evaluation (Debugger Recommended)**:
   - **Option A (Debugger)**:
     1. Add a configuration for `evaluate.py` to `.vscode/launch.json`.
     2. Select it and press F5.
   - **Option B (Terminal)**:
     ```powershell
     poetry run python evaluate.py
     ```
3. Add the resulting GIF to a `docs/` folder and link it from the README (screenshots motivate progress!).

---

### 4 . Experiment Tracking & Reflection
1. **Launch TensorBoard (Terminal Required)**:
   ```powershell
   poetry run tensorboard --logdir tb
   ```
2. Note observations in a `NOTES.md`