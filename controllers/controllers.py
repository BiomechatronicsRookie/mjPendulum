import mujoco
import numpy as np

def joint_pd_control(mj_Model, mj_Data):
  # Control constants and setpoint
  kp = 7.0
  kv = 1.0
  qpose_r = (np.pi/2, np.pi)
  
  # Same control values per joint
  if type(kp) == float and type(kv) == float :
    for i in range(len(mj_Data.ctrl)):
      mj_Data.ctrl[i] = -kp*(mj_Data.qpos[i] - qpose_r[i]) - kv*mj_Data.qvel[i]
      
  # Joint specific control values
  else:
    if len(kp) < len(mj_Data.qpos) or len(kv) < len(mj_Data.qvel):
      raise ValueError("Arrays must hold the same size")
    mj_Data.ctrl = -kp[i]*(mj_Data.qpos[i] - qpose_r[i]) - kv[i]*mj_Data.qvel[i]

  return

def random_controller(mj_Model, mj_Data):
  k = 0
  mj_Data.ctrl[0] = k*(np.random.rand() - 0.5)/0.5
  return