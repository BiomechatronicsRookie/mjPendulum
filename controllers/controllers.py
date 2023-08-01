import mujoco
import numpy as np

def pd_control(mj_Model, mj_Data):
  # Control constants
  kp = 7.0
  kv = 1.0
  # Setpoint (radians)
  qpose_r = (np.pi/2, np.pi)

  mj_Data.ctrl[0] = -kp*(mj_Data.qpos[0] - qpose_r[0]) - kv*mj_Data.qvel[0]
  mj_Data.ctrl[1] = -kp*(mj_Data.qpos[1] - qpose_r[1]) - kv*mj_Data.qvel[1]

  return

def random_controller(mj_Model, mj_Data):
  k = 0
  mj_Data.ctrl[0] = k*(np.random.rand() - 0.5)/0.5
  return