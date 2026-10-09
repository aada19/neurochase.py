# NEUROCHASE — Adaptive AI Maze Game

A browser-based, self-contained Class 11 AI Club exhibition project. Play at [GitHub Pages](https://aada19.github.io/neurochase.py/) after Pages is enabled.

## Features
- Maze exploration: **WASD / arrow keys**, mobile touch arrows
- Robot hunter that uses **shortest-path navigation** plus player-movement prediction
- Context-aware movement probabilities (robot's relative position and distance)
- Three stages: searching (0–19 moves), adapting (20–64), predicting (65+)
- Genuine prediction tracking (predictions are evaluated before model updates)
- Visible AI Brain dashboard, prediction confidence, behaviour percentages, learning cycles and Show AI modal
- Score, three lives, multiple rounds; model retained across rounds until Reset
- **No cloud AI calls, paid keys, libraries, or server required.** This is a transparent probability-based adaptive model, not a trained neural network or reinforcement-learning agent.

## Launch
Open `index.html` in any modern browser.

## Publish with GitHub Pages
1. Open **Settings → Pages** in the repository.
2. Under **Build and deployment**, select **Deploy from a branch**.
3. Choose **main**, **/(root)**, then **Save**.
4. GitHub should publish the site at `https://aada19.github.io/neurochase.py/`.

## Controls
- Arrows or WASD: move
- Space: pause/resume
- B: Show AI panel
- Show AI: pause and inspect the model
- Reset: restart and erase learned behaviour

## How the intelligence works
Before each valid movement the algorithm predicts a direction from a smoothed frequency table keyed by the robot's relative horizontal/vertical direction and proximity to the player. It then compares its prediction to the actual move and updates counts. When pursuing the player, its shortest-path navigation can target the predicted position (when reachable) at higher stages.

The pre-existing `maincode` Pygame version is left unchanged as a separate desktop prototype.
