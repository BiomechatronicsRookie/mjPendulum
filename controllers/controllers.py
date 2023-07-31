import mujoco
import numpy as np

def pd_control(mj_Model, mj_Data):
  kp = 8.0
  kv = 0.05
  mj_Data.ctrl[0] = -kp*mj_Data.qpos[0] - kv*mj_Data.qvel[0]
  mj_Data.ctrl[1] = -kp*mj_Data.qpos[1] - kv*mj_Data.qvel[1]
  return