import ale_py
_ = ale_py # Explicitly "use" the import to satisfy the linter
import numpy as np
import numpy.typing as npt
import gymnasium
from gymnasium.utils.play import play # type: ignore
import pygame
import sys
from typing import Optional, Tuple, Dict, Union

# Define precise types for observations and actions
ObsType = npt.NDArray[np.uint8]
ActType = int

# Define keyboard actions with correct types
KeyTuple = Tuple[Union[int, str], ...]
KeyType = Union[int, str, KeyTuple]
ActionMapType = Dict[KeyType, ActType]

keys_to_action: ActionMapType = {
    (pygame.K_SPACE,): 1,  # FIRE
    (pygame.K_LEFT,): 3,  # Try RIGHT action for LEFT key
    (pygame.K_RIGHT,): 2, # Try LEFT action for RIGHT key
    (pygame.K_LEFT, pygame.K_SPACE): 5,  # Try RIGHTFIRE for LEFT key + FIRE
    (pygame.K_RIGHT, pygame.K_SPACE): 4, # Try LEFTFIRE for RIGHT key + FIRE
}

env: Optional[gymnasium.Env[ObsType, ActType]] = None
try:
    env = gymnasium.make( # type: ignore
        "ALE/SpaceInvaders-v5", 
        render_mode="rgb_array", 
        frameskip=1
    ) # type: ignore
    print("Successfully created environment. Starting interactive play...")
    print("Controls: Left/Right Arrows, Space to Fire. Close window or Ctrl+C to quit.")

    play(env, keys_to_action=keys_to_action, fps=60, zoom=3)

    print("Play finished.")

except Exception as e:
    print(f"An error occurred: {e}", file=sys.stderr)
finally:
    if env is not None:
        env.close()
        print("Environment closed.") 