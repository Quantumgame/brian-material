from brian2 import *

#set_device('cpp_standalone')

tau = 5*ms
sigma = 0.3
eqs = '''
dv/dt = -v/tau + sigma*xi/tau**0.5 : 1
'''

G = NeuronGroup(1, eqs)

M = StateMonitor(G, 'v', record=True)

run(100*ms)

# This is ignored if the device is set to runtime
device.build(project_dir='standalone_example',
             compile_project=True, run_project=True)

plot(M.t/ms, M.v[0])
xlabel('Time (ms)')
ylabel('v')
show()
