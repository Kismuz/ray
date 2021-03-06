from ray.rllib.agents.ppo.ppo import PPOTrainer, DEFAULT_CONFIG
from ray.rllib.agents.ppo.appo import APPOTrainer
from ray.rllib.utils import renamed_class

PPOAgent = renamed_class(PPOTrainer)

__all__ = ["PPOAgent", "APPOTrainer", "PPOTrainer", "DEFAULT_CONFIG"]
