import time
import numpy as np
import mujoco
import mujoco.viewer
from controllers.controllers import *

def set_initial_conditions(mjData):
  mjData.qpos = np.random.rand(2)*np.pi
  return mjData

 
m = mujoco.MjModel.from_xml_path(r'.\model\scene.xml')
d = mujoco.MjData(m)

controller = mujoco.set_mjcb_control(pd_control)
d = set_initial_conditions(d)


with mujoco.viewer.launch_passive(m, d) as viewer:
  # Close the viewer automatically after 30 wall-seconds.
  start = time.time()
  while viewer.is_running():
    step_start = time.time()

    # mj_step can be replaced with code that also evaluates
    # a policy and applies a control signal before stepping the physics.
    mujoco.mj_step(m, d)
    # Pick up changes to the physics state, apply perturbations, update options from GUI.
    viewer.sync()

    # Rudimentary time keeping, will drift relative to wall clock.
    time_until_next_step = m.opt.timestep - (time.time() - step_start)
    if time_until_next_step > 0:
      time.sleep(time_until_next_step)