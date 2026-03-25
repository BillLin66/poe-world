from typing import Tuple, List, Any, Optional
import pickle

from classes.helper import ObjList, GameState
from path_utils import with_data_root


def load_atari_observations(
        identifier: str,
        config: Optional[Any] = None) -> Tuple[List[ObjList], List[str], List[GameState]]:
    filename = with_data_root(config, f'saved_data/obs_{identifier}.pickle')
    with open(filename, "rb") as f:
        observations, actions, game_states = pickle.load(f)
    return observations, actions, game_states
