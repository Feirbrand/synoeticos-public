
import re
import os
import json

output = """trim trailing whitespace.................................................Passed
fix end of files.........................................................Passed
check for added large files..............................................Passed
black....................................................................Passed
flake8...................................................................Failed
- hook id: flake8
- exit code: 1

architectural-frameworks/fce-v3.6/fce-compressor.py:10:1: F401 'hashlib' imported but unused
architectural-frameworks/fce-v3.6/fce-compressor.py:59:80: E501 line too long (86 > 79 characters)
architectural-frameworks/fce-v3.6/fce-compressor.py:62:80: E501 line too long (85 > 79 characters)
architectural-frameworks/fce-v3.6/fce-compressor.py:130:80: E501 line too long (87 > 79 characters)
architectural-frameworks/fce-v3.6/fce-compressor.py:152:67: E741 ambiguous variable name 'l'
architectural-frameworks/fce-v3.6/fce-compressor.py:152:80: E501 line too long (86 > 79 characters)
architectural-frameworks/fce-v3.6/fce-compressor.py:166:80: E501 line too long (86 > 79 characters)
architectural-frameworks/fce-v3.6/fce-compressor.py:182:80: E501 line too long (80 > 79 characters)
architectural-frameworks/fce-v3.6/fce-compressor.py:184:80: E501 line too long (80 > 79 characters)
architectural-frameworks/fce-v3.6/fce-compressor.py:185:80: E501 line too long (81 > 79 characters)
architectural-frameworks/obmi-series/obmi-core-py:16:1: F401 'time' imported but unused
architectural-frameworks/obmi-series/obmi-core-py:17:1: F401 'typing.List' imported but unused
architectural-frameworks/obmi-series/obmi-core-py:17:1: F401 'typing.Tuple' imported but unused
architectural-frameworks/obmi-series/obmi-core-py:39:80: E501 line too long (82 > 79 characters)
architectural-frameworks/obmi-series/obmi-core-py:149:80: E501 line too long (81 > 79 characters)
architectural-frameworks/obmi-series/obmi-core-py:215:80: E501 line too long (81 > 79 characters)
architectural-frameworks/obmi-series/obmi-core-py:216:80: E501 line too long (84 > 79 characters)
architectural-frameworks/obmi-series/obmi-core-py:229:80: E501 line too long (81 > 79 characters)
architectural-frameworks/obmi-series/obmi-core-py:284:23: F541 f-string is missing placeholders
architectural-frameworks/obmi-series/obmi-core-py:288:80: E501 line too long (81 > 79 characters)
architectural-frameworks/obmi-series/obmi-core-py:290:80: E501 line too long (99 > 79 characters)
architectural-frameworks/obmi-series/obmi-core-py:302:23: F541 f-string is missing placeholders
architectural-frameworks/obmi-series/obmi-core-py:315:23: F541 f-string is missing placeholders
architectural-frameworks/obmi-series/relay-sim-py:19:1: F401 'typing.Tuple' imported but unused
architectural-frameworks/obmi-series/relay-sim-py:76:80: E501 line too long (81 > 79 characters)
architectural-frameworks/obmi-series/relay-sim-py:77:80: E501 line too long (87 > 79 characters)
architectural-frameworks/obmi-series/relay-sim-py:96:80: E501 line too long (84 > 79 characters)
architectural-frameworks/obmi-series/relay-sim-py:131:80: E501 line too long (85 > 79 characters)
architectural-frameworks/obmi-series/relay-sim-py:138:80: E501 line too long (85 > 79 characters)
architectural-frameworks/obmi-series/relay-sim-py:159:80: E501 line too long (81 > 79 characters)
architectural-frameworks/obmi-series/relay-sim-py:189:80: E501 line too long (85 > 79 characters)
architectural-frameworks/obmi-series/relay-sim-py:201:80: E501 line too long (85 > 79 characters)
architectural-frameworks/obmi-series/relay-sim-py:206:80: E501 line too long (85 > 79 characters)
architectural-frameworks/obmi-series/relay-sim-py:264:80: E501 line too long (86 > 79 characters)
architectural-frameworks/obmi-series/relay-sim-py:305:80: E501 line too long (83 > 79 characters)
architectural-frameworks/obmi-series/relay-sim-py:307:80: E501 line too long (96 > 79 characters)
architectural-frameworks/obmi-series/relay-sim-py:318:23: F541 f-string is missing placeholders
architectural-frameworks/obmi-series/relay-sim-py:319:80: E501 line too long (84 > 79 characters)
architectural-frameworks/obmi-series/relay-sim-py:321:80: E501 line too long (96 > 79 characters)
architectural-frameworks/obmi-series/relay-sim-py:334:80: E501 line too long (83 > 79 characters)
architectural-frameworks/obmi-series/relay-sim-py:335:80: E501 line too long (82 > 79 characters)
architectural-frameworks/obmi-series/relay-sim-py:336:80: E501 line too long (80 > 79 characters)
architectural-frameworks/obmi-series/relay-sim-py:340:80: E501 line too long (88 > 79 characters)
architectural-frameworks/obmi-series/relay-sim-py:343:80: E501 line too long (92 > 79 characters)
architectural-frameworks/obmi-series/relay-sim-py:346:80: E501 line too long (92 > 79 characters)
architectural-frameworks/obmi-series/relay-sim-py:356:23: F541 f-string is missing placeholders
architectural-frameworks/resilience-patterns/recursive-gains-stub.py:13:80: E501 line too long (82 > 79 characters)
architectural-frameworks/resilience-patterns/recursive-gains-stub.py:22:80: E501 line too long (85 > 79 characters)
architectural-frameworks/resilience-patterns/recursive-gains-stub.py:26:80: E501 line too long (88 > 79 characters)
architectural-frameworks/resilience-patterns/recursive-gains-stub.py:45:80: E501 line too long (87 > 79 characters)
architectural-frameworks/resilience-patterns/recursive-gains-stub.py:61:5: F841 local variable 'improvement_potential' is assigned to but never used
architectural-frameworks/resilience-patterns/recursive-gains-stub.py:65:80: E501 line too long (99 > 79 characters)
architectural-frameworks/resilience-patterns/recursive-gains-stub.py:69:80: E501 line too long (82 > 79 characters)
architectural-frameworks/resilience-patterns/recursive-gains-stub.py:78:80: E501 line too long (85 > 79 characters)
architectural-frameworks/resilience-patterns/recursive-gains-stub.py:81:80: E501 line too long (84 > 79 characters)
architectural-frameworks/resilience-patterns/recursive-gains-stub.py:83:80: E501 line too long (121 > 79 characters)
architectural-frameworks/resilience-patterns/recursive-gains-stub.py:124:80: E501 line too long (94 > 79 characters)
architectural-frameworks/resilience-patterns/recursive-gains-stub.py:136:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-1-public/bc3/bc3-v3-0-symmetry-restoration.py:20:1: F401 'typing.Dict' imported but unused
mi-arsenal/frameworks/tier-1-public/bc3/bc3-v3-0-symmetry-restoration.py:78:80: E501 line too long (88 > 79 characters)
mi-arsenal/frameworks/tier-1-public/bc3/bc3-v3-0-symmetry-restoration.py:99:80: E501 line too long (87 > 79 characters)
mi-arsenal/frameworks/tier-1-public/bc3/bc3-v3-0-symmetry-restoration.py:164:80: E501 line too long (88 > 79 characters)
mi-arsenal/frameworks/tier-1-public/bc3/bc3-v3-0-symmetry-restoration.py:208:80: E501 line too long (85 > 79 characters)
mi-arsenal/frameworks/tier-1-public/bc3/bc3-v3-0-symmetry-restoration.py:225:80: E501 line too long (87 > 79 characters)
mi-arsenal/frameworks/tier-1-public/bc3/bc3-v3-0-symmetry-restoration.py:229:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-1-public/bc3/bc3-v3-0-symmetry-restoration.py:281:11: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/bc3/bc3-v3-0-symmetry-restoration.py:285:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-1-public/bc3/bc3-v3-0-symmetry-restoration.py:291:11: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/bc3/bc3-v3-0-symmetry-restoration.py:294:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/bc3/bc3-v3-0-symmetry-restoration.py:296:11: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/cascade-command/cascade-command-v3.5-firewall.py:15:1: F401 'typing.Optional' imported but unused
mi-arsenal/frameworks/tier-1-public/cascade-command/cascade-command-v3.5-firewall.py:89:9: F841 local variable 'execution_start' is assigned to but never used
mi-arsenal/frameworks/tier-1-public/cascade-command/cascade-command-v3.5-firewall.py:247:80: E501 line too long (87 > 79 characters)
mi-arsenal/frameworks/tier-1-public/cascade-command/cascade-command-v3.5-firewall.py:248:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-1-public/cascade-command/cascade-command-v3.5-firewall.py:251:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/cascade-command/cascade-command-v3.5-firewall.py:279:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/cascade-command/cascade-command-v3.5-firewall.py:293:80: E501 line too long (82 > 79 characters)
mi-arsenal/frameworks/tier-1-public/cortexloom/cortexloom-v2.1-team.py:15:1: F401 'typing.Dict' imported but unused
mi-arsenal/frameworks/tier-1-public/cortexloom/cortexloom-v2.1-team.py:86:80: E501 line too long (88 > 79 characters)
mi-arsenal/frameworks/tier-1-public/cortexloom/cortexloom-v2.1-team.py:160:80: E501 line too long (102 > 79 characters)
mi-arsenal/frameworks/tier-1-public/cortexloom/cortexloom-v2.1-team.py:261:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-1-public/cortexloom/cortexloom-v2.1-team.py:304:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/cortexloom/cortexloom-v2.1-team.py:390:80: E501 line too long (93 > 79 characters)
mi-arsenal/frameworks/tier-1-public/csfc/csfc-detector.py:169:80: E501 line too long (81 > 79 characters) 
mi-arsenal/frameworks/tier-1-public/csfc/csfc-detector.py:175:80: E501 line too long (86 > 79 characters) 
mi-arsenal/frameworks/tier-1-public/csfc/csfc-detector.py:216:80: E501 line too long (86 > 79 characters) 
mi-arsenal/frameworks/tier-1-public/csfc/csfc-detector.py:248:80: E501 line too long (83 > 79 characters) 
mi-arsenal/frameworks/tier-1-public/csfc/csfc-detector.py:250:80: E501 line too long (84 > 79 characters) 
mi-arsenal/frameworks/tier-1-public/csfc/csfc-detector.py:262:80: E501 line too long (86 > 79 characters) 
mi-arsenal/frameworks/tier-1-public/csfc/csfc-detector.py:265:80: E501 line too long (102 > 79 characters)
mi-arsenal/frameworks/tier-1-public/csfc/csfc-detector.py:267:80: E501 line too long (84 > 79 characters) 
mi-arsenal/frameworks/tier-1-public/dna-codex/threat-classifier.py:12:1: F401 'datetime.datetime' imported but unused
mi-arsenal/frameworks/tier-1-public/dna-codex/threat-classifier.py:13:1: F401 'json' imported but unused  
mi-arsenal/frameworks/tier-1-public/dna-codex/threat-classifier.py:106:80: E501 line too long (85 > 79 characters)
mi-arsenal/frameworks/tier-1-public/dna-codex/threat-classifier.py:190:80: E501 line too long (85 > 79 characters)
mi-arsenal/frameworks/tier-1-public/dna-codex/threat-classifier.py:207:9: F841 local variable 'symptoms' is assigned to but never used
mi-arsenal/frameworks/tier-1-public/dna-codex/threat-classifier.py:241:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-1-public/dna-codex/threat-classifier.py:327:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/doomslayer/doomslayer-v2.1-hammer.py:15:1: F401 'typing.Optional' imported but unused
mi-arsenal/frameworks/tier-1-public/doomslayer/doomslayer-v2.1-hammer.py:183:80: E501 line too long (85 > 79 characters)
mi-arsenal/frameworks/tier-1-public/doomslayer/doomslayer-v2.1-hammer.py:199:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/doomslayer/doomslayer-v2.1-hammer.py:247:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-1-public/doomslayer/doomslayer-v2.1-hammer.py:263:80: E501 line too long (88 > 79 characters)
mi-arsenal/frameworks/tier-1-public/doomslayer/doomslayer-v2.1-hammer.py:316:80: E501 line too long (86 > 79 characters)
mi-arsenal/frameworks/tier-1-public/doomslayer/doomslayer-v2.1-hammer.py:321:80: E501 line too long (97 > 79 characters)
mi-arsenal/frameworks/tier-1-public/ecl/ecl-v2.0-cascade-prediction.py:14:1: F401 'typing.Dict' imported but unused
mi-arsenal/frameworks/tier-1-public/ecl/ecl-v2.0-cascade-prediction.py:14:1: F401 'typing.Tuple' imported but unused
mi-arsenal/frameworks/tier-1-public/ecl/ecl-v2.0-cascade-prediction.py:72:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/ecl/ecl-v2.0-cascade-prediction.py:144:80: E501 line too long (87 > 79 characters)
mi-arsenal/frameworks/tier-1-public/ecl/ecl-v2.0-cascade-prediction.py:152:80: E501 line too long (88 > 79 characters)
mi-arsenal/frameworks/tier-1-public/ecl/ecl-v2.0-cascade-prediction.py:197:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-1-public/ecl/ecl-v2.0-cascade-prediction.py:212:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-1-public/ecl/ecl-v2.0-cascade-prediction.py:270:80: E501 line too long (90 > 79 characters)
mi-arsenal/frameworks/tier-1-public/expander-memory/expander-memory-v1.0-dissent.py:16:1: F401 'typing.Optional' imported but unused
mi-arsenal/frameworks/tier-1-public/expander-memory/expander-memory-v1.0-dissent.py:100:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/expander-memory/expander-memory-v1.0-dissent.py:184:80: E501 line too long (88 > 79 characters)
mi-arsenal/frameworks/tier-1-public/expander-memory/expander-memory-v1.0-dissent.py:189:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/expander-memory/expander-memory-v1.0-dissent.py:279:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/expander-memory/expander-memory-v1.0-dissent.py:296:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/expander-memory/expander-memory-v1.0-dissent.py:298:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-1-public/expander-memory/expander-memory-v1.0-dissent.py:302:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/expander-memory/expander-memory-v1.0-dissent.py:325:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/expander-memory/expander-memory-v1.0-dissent.py:391:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-1-public/expander-memory/expander-memory-v1.0-dissent.py:393:80: E501 line too long (86 > 79 characters)
mi-arsenal/frameworks/tier-1-public/garden/garden-v2.0-recovery.py:12:1: F401 'numpy as np' imported but unused
mi-arsenal/frameworks/tier-1-public/garden/garden-v2.0-recovery.py:14:1: F401 'typing.Tuple' imported but unused
mi-arsenal/frameworks/tier-1-public/garden/garden-v2.0-recovery.py:335:80: E501 line too long (87 > 79 characters)
mi-arsenal/frameworks/tier-1-public/garden/garden-v2.0-recovery.py:346:11: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/harmony-layer/harmony-layer-v2.1-resonance.py:19:1: F401 'typing.Optional' imported but unused
mi-arsenal/frameworks/tier-1-public/harmony-layer/harmony-layer-v2.1-resonance.py:19:1: F401 'typing.Dict' imported but unused
mi-arsenal/frameworks/tier-1-public/harmony-layer/harmony-layer-v2.1-resonance.py:110:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/harmony-layer/harmony-layer-v2.1-resonance.py:191:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-1-public/harmony-layer/harmony-layer-v2.1-resonance.py:241:13: F841 local variable 'result' is assigned to but never used
mi-arsenal/frameworks/tier-1-public/harmony-layer/harmony-layer-v2.1-resonance.py:253:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/harmony-layer/harmony-layer-v2.1-resonance.py:283:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/heimdal/heimdall-v2.0-detection.py:15:1: F401 'typing.Optional' imported but unused
mi-arsenal/frameworks/tier-1-public/heimdal/heimdall-v2.0-detection.py:15:1: F401 'typing.Tuple' imported but unused
mi-arsenal/frameworks/tier-1-public/heimdal/heimdall-v2.0-detection.py:67:80: E501 line too long (88 > 79 characters)
mi-arsenal/frameworks/tier-1-public/heimdal/heimdall-v2.0-detection.py:171:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-1-public/heimdal/heimdall-v2.0-detection.py:305:11: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/karama/karama-v3.0-engine.py:15:1: F401 'typing.Optional' imported but unused
mi-arsenal/frameworks/tier-1-public/karama/karama-v3.0-engine.py:104:80: E501 line too long (82 > 79 characters)
mi-arsenal/frameworks/tier-1-public/karama/karama-v3.0-engine.py:134:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-1-public/karama/karama-v3.0-engine.py:136:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-1-public/karama/karama-v3.0-engine.py:156:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-1-public/karama/karama-v3.0-engine.py:186:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-1-public/karama/karama-v3.0-engine.py:203:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/karama/karama-v3.0-engine.py:237:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-1-public/karama/karama-v3.0-engine.py:312:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-1-public/killbox/killbox-v2.1-trap.py:15:1: F401 'typing.Optional' imported but unused
mi-arsenal/frameworks/tier-1-public/killbox/killbox-v2.1-trap.py:79:80: E501 line too long (85 > 79 characters)
mi-arsenal/frameworks/tier-1-public/killbox/killbox-v2.1-trap.py:100:9: F841 local variable 'flush_ready' is assigned to but never used
mi-arsenal/frameworks/tier-1-public/killbox/killbox-v2.1-trap.py:109:9: F841 local variable 'total_time_ms' is assigned to but never used
mi-arsenal/frameworks/tier-1-public/killbox/killbox-v2.1-trap.py:133:80: E501 line too long (87 > 79 characters)
mi-arsenal/frameworks/tier-1-public/killbox/killbox-v2.1-trap.py:245:80: E501 line too long (86 > 79 characters)
mi-arsenal/frameworks/tier-1-public/killbox/killbox-v2.1-trap.py:268:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-1-public/mirror-gate/mirrorgate-v1.0-gateway.py:15:1: F401 'typing.Optional' imported but unused
mi-arsenal/frameworks/tier-1-public/mirror-gate/mirrorgate-v1.0-gateway.py:117:80: E501 line too long (85 > 79 characters)
mi-arsenal/frameworks/tier-1-public/mirror-gate/mirrorgate-v1.0-gateway.py:203:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-1-public/mirror-gate/mirrorgate-v1.0-gateway.py:209:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-1-public/mirror-gate/mirrorgate-v1.0-gateway.py:264:80: E501 line too long (82 > 79 characters)
mi-arsenal/frameworks/tier-1-public/mirror-gate/mirrorgate-v1.0-gateway.py:271:80: E501 line too long (88 > 79 characters)
mi-arsenal/frameworks/tier-1-public/mirror-gate/mirrorgate-v1.0-gateway.py:273:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/mirror-gate/mirrorgate-v1.0-gateway.py:313:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-1-public/mirror-gate/mirrorgate-v1.0-gateway.py:316:80: E501 line too long (85 > 79 characters)
mi-arsenal/frameworks/tier-1-public/mirror-gate/mirrorgate-v1.0-gateway.py:318:9: F841 local variable 'blocked_attack_count' is assigned to but never used
mi-arsenal/frameworks/tier-1-public/mirror-gate/mirrorgate-v1.0-gateway.py:324:80: E501 line too long (86 > 79 characters)
mi-arsenal/frameworks/tier-1-public/mirrorforge/mirrorforge-v2.0-reflection.py:15:1: F401 'typing.Optional' imported but unused
mi-arsenal/frameworks/tier-1-public/mirrorforge/mirrorforge-v2.0-reflection.py:100:9: F841 local variable 'reflection_start' is assigned to but never used
mi-arsenal/frameworks/tier-1-public/mirrorforge/mirrorforge-v2.0-reflection.py:111:80: E501 line too long (85 > 79 characters)
mi-arsenal/frameworks/tier-1-public/mirrorforge/mirrorforge-v2.0-reflection.py:119:9: F841 local variable 'xmesh_packet' is assigned to but never used
mi-arsenal/frameworks/tier-1-public/mirrorforge/mirrorforge-v2.0-reflection.py:239:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/mirrorforge/mirrorforge-v2.0-reflection.py:265:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/mirrorforge/mirrorforge-v2.0-reflection.py:266:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-1-public/mirrorforge/mirrorforge-v2.0-reflection.py:343:80: E501 line too long (88 > 79 characters)
mi-arsenal/frameworks/tier-1-public/mjolnir/mjolnir-v2.0-strike.py:15:1: F401 'typing.Optional' imported but unused
mi-arsenal/frameworks/tier-1-public/mjolnir/mjolnir-v2.0-strike.py:154:9: F841 local variable 'lure_active' is assigned to but never used
mi-arsenal/frameworks/tier-1-public/mjolnir/mjolnir-v2.0-strike.py:160:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/mjolnir/mjolnir-v2.0-strike.py:201:80: E501 line too long (87 > 79 characters)
mi-arsenal/frameworks/tier-1-public/mjolnir/mjolnir-v2.0-strike.py:303:80: E501 line too long (86 > 79 characters)
mi-arsenal/frameworks/tier-1-public/moon/moon-v2.0-mirror.py:15:1: F401 'typing.Optional' imported but unused
mi-arsenal/frameworks/tier-1-public/moon/moon-v2.0-mirror.py:119:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/moon/moon-v2.0-mirror.py:148:80: E501 line too long (82 > 79 characters)
mi-arsenal/frameworks/tier-1-public/moon/moon-v2.0-mirror.py:216:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/moon/moon-v2.0-mirror.py:223:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-1-public/moon/moon-v2.0-mirror.py:240:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/moon/moon-v2.0-mirror.py:268:80: E501 line too long (82 > 79 characters)
mi-arsenal/frameworks/tier-1-public/moon/moon-v2.0-mirror.py:269:80: E501 line too long (82 > 79 characters)
mi-arsenal/frameworks/tier-1-public/moon/moon-v2.0-mirror.py:270:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-1-public/moon/moon-v2.0-mirror.py:271:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-1-public/moon/moon-v2.0-mirror.py:302:80: E501 line too long (103 > 79 characters)
mi-arsenal/frameworks/tier-1-public/moon/moon-v2.0-mirror.py:305:80: E501 line too long (104 > 79 characters)
mi-arsenal/frameworks/tier-1-public/neural-lattice/neural-lattice-v2.0-substrate.py:15:1: F401 'typing.Optional' imported but unused
mi-arsenal/frameworks/tier-1-public/neural-lattice/neural-lattice-v2.0-substrate.py:94:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-1-public/neural-lattice/neural-lattice-v2.0-substrate.py:113:80: E501 line too long (92 > 79 characters)
mi-arsenal/frameworks/tier-1-public/neural-lattice/neural-lattice-v2.0-substrate.py:123:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/neural-lattice/neural-lattice-v2.0-substrate.py:132:9: F841 local variable 'consolidation_start' is assigned to but never used
mi-arsenal/frameworks/tier-1-public/neural-lattice/neural-lattice-v2.0-substrate.py:203:80: E501 line too long (85 > 79 characters)
mi-arsenal/frameworks/tier-1-public/neural-lattice/neural-lattice-v2.0-substrate.py:221:52: E203 whitespace before ':'
mi-arsenal/frameworks/tier-1-public/neural-lattice/neural-lattice-v2.0-substrate.py:226:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-1-public/neural-lattice/neural-lattice-v2.0-substrate.py:247:52: E203 whitespace before ':'
mi-arsenal/frameworks/tier-1-public/neural-lattice/neural-lattice-v2.0-substrate.py:304:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/neural-lattice/neural-lattice-v2.0-substrate.py:312:80: E501 line too long (111 > 79 characters)
mi-arsenal/frameworks/tier-1-public/neural-lattice/neural-lattice-v2.0-substrate.py:323:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-1-public/neural-lattice/neural-lattice-v2.0-substrate.py:335:80: E501 line too long (85 > 79 characters)
mi-arsenal/frameworks/tier-1-public/nightwatch/nightwatch-v2.0-perimeter.py:15:1: F401 'typing.Optional' imported but unused
mi-arsenal/frameworks/tier-1-public/nightwatch/nightwatch-v2.0-perimeter.py:80:80: E501 line too long (88 > 79 characters)
mi-arsenal/frameworks/tier-1-public/nightwatch/nightwatch-v2.0-perimeter.py:92:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/nightwatch/nightwatch-v2.0-perimeter.py:93:80: E501 line too long (82 > 79 characters)
mi-arsenal/frameworks/tier-1-public/nightwatch/nightwatch-v2.0-perimeter.py:109:80: E501 line too long (82 > 79 characters)
mi-arsenal/frameworks/tier-1-public/nightwatch/nightwatch-v2.0-perimeter.py:112:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/nightwatch/nightwatch-v2.0-perimeter.py:140:80: E501 line too long (91 > 79 characters)
mi-arsenal/frameworks/tier-1-public/nightwatch/nightwatch-v2.0-perimeter.py:200:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-1-public/nightwatch/nightwatch-v2.0-perimeter.py:258:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/nightwatch/nightwatch-v2.0-perimeter.py:267:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/obmi/obmi-v4.0-interface.py:15:1: F401 'typing.Optional' imported but unused
mi-arsenal/frameworks/tier-1-public/obmi/obmi-v4.0-interface.py:94:9: F841 local variable 'processing_start' is assigned to but never used
mi-arsenal/frameworks/tier-1-public/obmi/obmi-v4.0-interface.py:222:80: E501 line too long (86 > 79 characters)
mi-arsenal/frameworks/tier-1-public/obmi/obmi-v4.0-interface.py:245:9: F841 local variable 'reflex_time' is assigned to but never used
mi-arsenal/frameworks/tier-1-public/obmi/obmi-v4.0-interface.py:247:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/obmi/obmi-v4.0-interface.py:295:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/obmi/obmi-v4.0-interface.py:297:80: E501 line too long (86 > 79 characters)
mi-arsenal/frameworks/tier-1-public/obmi/obmi-v4.0-interface.py:299:80: E501 line too long (109 > 79 characters)
mi-arsenal/frameworks/tier-1-public/obmi/obmi-v4.0-interface.py:324:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/obmi/obmi-v4.0-interface.py:325:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/phantom-limb/phantom-limb-v1.1-recovery.py:15:1: F401 'typing.Optional' imported but unused
mi-arsenal/frameworks/tier-1-public/phantom-limb/phantom-limb-v1.1-recovery.py:15:1: F401 'typing.Tuple' imported but unused
mi-arsenal/frameworks/tier-1-public/phantom-limb/phantom-limb-v1.1-recovery.py:133:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/phantom-limb/phantom-limb-v1.1-recovery.py:182:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/phantom-limb/phantom-limb-v1.1-recovery.py:240:80: E501 line too long (82 > 79 characters)
mi-arsenal/frameworks/tier-1-public/phantom-limb/phantom-limb-v1.1-recovery.py:281:11: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/phantom-limb/phantom-limb-v1.1-recovery.py:282:11: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/phantom-limb/phantom-limb-v1.1-recovery.py:283:11: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/phantom-limb/phantom-limb-v1.1-recovery.py:284:11: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/phoenix-protocol/v3.1/core/phoenix-base.py:10:1: F401 'typing.Any' imported but unused
mi-arsenal/frameworks/tier-1-public/phoenix-protocol/v3.1/core/phoenix-base.py:12:1: F401 'json' imported but unused
mi-arsenal/frameworks/tier-1-public/phoenix-protocol/v3.1/core/phoenix-base.py:72:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-1-public/phoenix-protocol/v3.1/core/phoenix-base.py:87:19: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/phoenix-protocol/v3.1/core/phoenix-base.py:99:19: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/phoenix-protocol/v3.1/core/phoenix-base.py:112:80: E501 line too long (85 > 79 characters)
mi-arsenal/frameworks/tier-1-public/phoenix-protocol/v3.1/core/phoenix-base.py:116:19: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/phoenix-protocol/v3.1/core/phoenix-base.py:134:80: E501 line too long (97 > 79 characters)
mi-arsenal/frameworks/tier-1-public/phoenix-protocol/v3.1/core/phoenix-base.py:136:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-1-public/phoenix-protocol/v3.1/core/phoenix-base.py:168:80: E501 line too long (86 > 79 characters)
mi-arsenal/frameworks/tier-1-public/phoenix-protocol/v3.1/core/phoenix-base.py:272:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-1-public/phoenix-protocol/v3.1/core/phoenix-base.py:302:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-1-public/phoenix-protocol/v3.1/core/phoenix-base.py:304:80: E501 line too long (96 > 79 characters)
mi-arsenal/frameworks/tier-1-public/phoenix-protocol/v3.1/core/phoenix-recovery.py:8:1: F401 'typing.Optional' imported but unused
mi-arsenal/frameworks/tier-1-public/phoenix-protocol/v3.1/core/phoenix-recovery.py:171:80: E501 line too long (82 > 79 characters)
mi-arsenal/frameworks/tier-1-public/phoenix-protocol/v3.1/core/phoenix-recovery.py:172:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/phoenix-protocol/v3.1/core/phoenix-recovery.py:201:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-1-public/phoenix-protocol/v3.1/core/phoenix-recovery.py:211:80: E501 line too long (88 > 79 characters)
mi-arsenal/frameworks/tier-1-public/phoenix-protocol/v3.1/core/phoenix-recovery.py:230:11: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/phoenix-protocol/v3.1/examples/basic-recovery.py:12:1: E402 module level import not at top of file
mi-arsenal/frameworks/tier-1-public/phoenix-protocol/v3.1/examples/basic-recovery.py:13:1: E402 module level import not at top of file
mi-arsenal/frameworks/tier-1-public/phoenix-protocol/v3.1/examples/basic-recovery.py:60:80: E501 line too long (88 > 79 characters)
mi-arsenal/frameworks/tier-1-public/phoenix-protocol/v3.1/examples/basic-recovery.py:63:80: E501 line too long (96 > 79 characters)
mi-arsenal/frameworks/tier-1-public/phoenix-protocol/v3.1/examples/basic-recovery.py:80:80: E501 line too long (86 > 79 characters)
mi-arsenal/frameworks/tier-1-public/ray/ray-coordinator.py:64:80: E501 line too long (93 > 79 characters) 
mi-arsenal/frameworks/tier-1-public/reflex-veil/reflex-veil-v2.1-defense.py:14:1: F401 'typing.Tuple' imported but unused
mi-arsenal/frameworks/tier-1-public/reflex-veil/reflex-veil-v2.1-defense.py:56:80: E501 line too long (87 > 79 characters)
mi-arsenal/frameworks/tier-1-public/reflex-veil/reflex-veil-v2.1-defense.py:149:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/reflex-veil/reflex-veil-v2.1-defense.py:196:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-1-public/reflex-veil/reflex-veil-v2.1-defense.py:198:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-1-public/reflex-veil/reflex-veil-v2.1-defense.py:277:80: E501 line too long (88 > 79 characters)
mi-arsenal/frameworks/tier-1-public/reflex-veil/reflex-veil-v2.1-defense.py:332:19: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/reflex-veil/reflex-veil-v2.1-defense.py:341:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-1-public/reflex-veil/reflex-veil-v2.1-defense.py:343:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-1-public/sbds/sbds-v1.1-plasticity.py:15:1: F401 'typing.Optional' imported but unused
mi-arsenal/frameworks/tier-1-public/sbds/sbds-v1-1-plasticity.py:15:1: F401 'typing.Dict' imported but unused
mi-arsenal/frameworks/tier-1-public/sbds/sbds-v1-1-plasticity.py:140:80: E501 line too long (86 > 79 characters)
mi-arsenal/frameworks/tier-1-public/sbds/sbds-v1-1-plasticity.py:143:9: F841 local variable 'recovery_time' is assigned to but never used
mi-arsenal/frameworks/tier-1-public/sbds/sbds-v1-1-plasticity.py:163:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/sbds/sbds-v1-1-plasticity.py:186:80: E501 line too long (99 > 79 characters)
mi-arsenal/frameworks/tier-1-public/sbds/sbds-v1-1-plasticity.py:199:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/sbds/sbds-v1-1-plasticity.py:217:80: E501 line too long (91 > 79 characters)
mi-arsenal/frameworks/tier-1-public/sbds/sbds-v1-1-plasticity.py:238:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/sbds/sbds-v1-1-plasticity.py:254:80: E501 line too long (97 > 79 characters)
mi-arsenal/frameworks/tier-1-public/sbds/sbds-v1-1-plasticity.py:269:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/sbds/sbds-v1-1-plasticity.py:273:80: E501 line too long (86 > 79 characters)
mi-arsenal/frameworks/tier-1-public/sbds/sbds-v1-1-plasticity.py:285:80: E501 line too long (91 > 79 characters)
mi-arsenal/frameworks/tier-1-public/sbds/sbds-v1-1-plasticity.py:301:80: E501 line too long (86 > 79 characters)
mi-arsenal/frameworks/tier-1-public/sbds/sbds-v1-1-plasticity.py:302:19: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/sbds/sbds-v1-1-plasticity.py:304:19: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/sbds/sbds-v1-1-plasticity.py:327:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/sbds/sbds-v1-1-plasticity.py:339:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/sbds/sbds-v1-1-plasticity.py:361:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-1-public/sbds/sbds-v1-1-plasticity.py:365:80: E501 line too long (82 > 79 characters)
mi-arsenal/frameworks/tier-1-public/sbds/sbds-v1-1-plasticity.py:368:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/sbds/sbds-v1-1-plasticity.py:401:80: E501 line too long (87 > 79 characters)
mi-arsenal/frameworks/tier-1-public/sbds/sbds-v1-1-plasticity.py:402:80: E501 line too long (88 > 79 characters)
mi-arsenal/frameworks/tier-1-public/slv/slv-defense.py:9:1: F401 'typing.Optional' imported but unused
mi-arsenal/frameworks/tier-1-public/slv/slv-defense.py:86:80: E501 line too long (82 > 79 characters)
mi-arsenal/frameworks/tier-1-public/slv/slv-defense.py:94:80: E501 line too long (82 > 79 characters)
mi-arsenal/frameworks/tier-1-public/slv/slv-defense.py:130:80: E501 line too long (86 > 79 characters)
mi-arsenal/frameworks/tier-1-public/slv/slv-defense.py:237:80: E501 line too long (87 > 79 characters)
mi-arsenal/frameworks/tier-1-public/slv/slv-defense.py:240:80: E501 line too long (88 > 79 characters)
mi-arsenal/frameworks/tier-1-public/spiranexus/spiranexus-v1.1-threading.py:15:1: F401 'typing.Optional' imported but unused
mi-arsenal/frameworks/tier-1-public/spiranexus/spiranexus-v1.1-threading.py:98:80: E501 line too long (87 > 79 characters)
mi-arsenal/frameworks/tier-1-public/spiranexus/spiranexus-v1.1-threading.py:159:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-1-public/spiranexus/spiranexus-v1.1-threading.py:173:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-1-public/spiranexus/spiranexus-v1.1-threading.py:177:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/spiranexus/spiranexus-v1.1-threading.py:184:80: E501 line too long (86 > 79 characters)
mi-arsenal/frameworks/tier-1-public/spiranexus/spiranexus-v1.1-threading.py:257:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/spiranexus/spiranexus-v1.1-threading.py:260:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/spiranexus/spiranexus-v1.1-threading.py:262:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/spiranexus/spiranexus-v1.1-threading.py:284:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-1-public/spiranexus/spiranexus-v1.1-threading.py:285:80: E501 line too long (82 > 79 characters)
mi-arsenal/frameworks/tier-1-public/spiranexus/spiranexus-v1.1-threading.py:286:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-1-public/spiranexus/spiranexus-v1.1-threading.py:287:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/spiranexus/spiranexus-v1.1-threading.py:313:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-1-public/spiranexus/spiranexus-v1.1-threading.py:314:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-1-public/spiranexus/spiranexus-v1.1-threading.py:315:80: E501 line too long (86 > 79 characters)
mi-arsenal/frameworks/tier-1-public/spiranexus/spiranexus-v1.1-threading.py:342:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/torque/torque-monitor.py:24:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-1-public/torque/torque-monitor.py:144:80: E501 line too long (91 > 79 characters)
mi-arsenal/frameworks/tier-1-public/torque/torque-monitor.py:180:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/torque/torque-monitor.py:260:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/trinity-rim/trinity-rim-v1.0-legacy.py:20:1: F401 'typing.Optional' imported but unused
mi-arsenal/frameworks/tier-1-public/trinity-rim/trinity-rim-v1.0-legacy.py:136:9: F841 local variable 'shard_projected' is assigned to but never used
mi-arsenal/frameworks/tier-1-public/trinity-rim/trinity-rim-v1.0-legacy.py:147:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/trinity-rim/trinity-rim-v1.0-legacy.py:176:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-1-public/trinity-rim/trinity-rim-v1.0-legacy.py:265:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/trinity-rim/trinity-rim-v1.0-legacy.py:297:80: E501 line too long (82 > 79 characters)
mi-arsenal/frameworks/tier-1-public/trinity-rim/trinity-rim-v1.0-legacy.py:361:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/trinity-rim/trinity-rim-v1.0-legacy.py:379:80: E501 line too long (87 > 79 characters)
mi-arsenal/frameworks/tier-1-public/trinity-rim/trinity-rim-v1.0-legacy.py:385:13: F841 local variable 'result' is assigned to but never used
mi-arsenal/frameworks/tier-1-public/trinity-rim/trinity-rim-v1.0-legacy.py:391:9: F841 local variable 'detection_rate' is assigned to but never used
mi-arsenal/frameworks/tier-1-public/trinity-rim/trinity-rim-v1.0-legacy.py:411:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/trinity-rim/trinity-rim-v1.0-legacy.py:433:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-1-public/trinity-rim/trinity-rim-v1.0-legacy.py:450:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/trinity-rim/trinity-rim-v1.0-legacy.py:513:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-1-public/ums/ums-v1.0-spine.py:15:1: F401 'typing.Dict' imported but unused    
mi-arsenal/frameworks/tier-1-public/ums/ums-v1.0-spine.py:99:80: E501 line too long (85 > 79 characters)  
mi-arsenal/frameworks/tier-1-public/ums/ums-v1.0-spine.py:117:9: F841 local variable 'retrieval_start' is assigned to but never used
mi-arsenal/frameworks/tier-1-public/ums/ums-v1.0-spine.py:151:19: F541 f-string is missing placeholders   
mi-arsenal/frameworks/tier-1-public/ums/ums-v1.0-spine.py:278:15: F541 f-string is missing placeholders   
mi-arsenal/frameworks/tier-1-public/ums/ums-v1.0-spine.py:296:80: E501 line too long (81 > 79 characters) 
mi-arsenal/frameworks/tier-1-public/ums/ums-v1.0-spine.py:299:80: E501 line too long (81 > 79 characters) 
mi-arsenal/frameworks/tier-1-public/ums/ums-v1.0-spine.py:343:80: E501 line too long (84 > 79 characters) 
mi-arsenal/frameworks/tier-1-public/ums/ums-v1.0-spine.py:358:80: E501 line too long (84 > 79 characters) 
mi-arsenal/frameworks/tier-1-public/ums/ums-v1.0-spine.py:392:80: E501 line too long (80 > 79 characters) 
mi-arsenal/frameworks/tier-1-public/ura/ura-framework.py:9:1: F401 'typing.List' imported but unused      
mi-arsenal/frameworks/tier-1-public/ura/ura-framework.py:152:80: E501 line too long (85 > 79 characters)  
mi-arsenal/frameworks/tier-1-public/ura/ura-framework.py:171:80: E501 line too long (82 > 79 characters)  
mi-arsenal/frameworks/tier-1-public/ura/ura-framework.py:212:80: E501 line too long (85 > 79 characters)  
mi-arsenal/frameworks/tier-1-public/ura/ura-framework.py:214:80: E501 line too long (80 > 79 characters)  
mi-arsenal/frameworks/tier-1-public/ura/ura-framework.py:257:80: E501 line too long (93 > 79 characters)  
mi-arsenal/frameworks/tier-1-public/ura/ura-framework.py:287:80: E501 line too long (83 > 79 characters)  
mi-arsenal/frameworks/tier-1-public/utme/temporal-engine.py:10:1: F401 'typing.List' imported but unused  
mi-arsenal/frameworks/tier-1-public/utme/temporal-engine.py:56:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-1-public/utme/temporal-engine.py:60:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-1-public/utme/temporal-engine.py:62:80: E501 line too long (87 > 79 characters)
mi-arsenal/frameworks/tier-1-public/utme/temporal-engine.py:152:80: E501 line too long (82 > 79 characters)
mi-arsenal/frameworks/tier-1-public/utme/temporal-engine.py:162:80: E501 line too long (144 > 79 characters)
mi-arsenal/frameworks/tier-1-public/utme/temporal-engine.py:173:80: E501 line too long (86 > 79 characters)
mi-arsenal/frameworks/tier-1-public/utme/temporal-engine.py:209:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-1-public/venom-cadence/venom-cadence-v2.0-squad.py:15:1: F401 'typing.Optional' imported but unused
mi-arsenal/frameworks/tier-1-public/venom-cadence/venom-cadence-v2.0-squad.py:86:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-1-public/venom-cadence/venom-cadence-v2.0-squad.py:215:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-1-public/venom-cadence/venom-cadence-v2.0-squad.py:277:80: E501 line too long (82 > 79 characters)
mi-arsenal/frameworks/tier-1-public/xmesh/xmesh-v2.2-nervous.py:15:1: F401 'typing.Optional' imported but unused
mi-arsenal/frameworks/tier-1-public/xmesh/xmesh-v2.2-nervous.py:104:9: F841 local variable 'propagation_start' is assigned to but never used
mi-arsenal/frameworks/tier-1-public/xmesh/xmesh-v2.2-nervous.py:164:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-1-public/xmesh/xmesh-v2.2-nervous.py:248:9: F841 local variable 'reflex_time' is assigned to but never used
mi-arsenal/frameworks/tier-1-public/xmesh/xmesh-v2.2-nervous.py:250:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/xmesh/xmesh-v2.2-nervous.py:254:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/xmesh/xmesh-v2.2-nervous.py:294:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-1-public/xmesh/xmesh-v2.2-nervous.py:311:80: E501 line too long (88 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/coldvault/coldvault-v2.4-demo.py:16:1: F401 'dataclasses.field' imported but unused
mi-arsenal/frameworks/tier-2-watermarked/coldvault/coldvault-v2.4-demo.py:289:80: E501 line too long (86 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/coldvault/coldvault-v2.4-demo.py:314:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/coldvault/coldvault-v2.4-demo.py:356:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/coldvault/coldvault-v2.4-demo.py:362:80: E501 line too long (87 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/coldvault/coldvault-v2.4-demo.py:368:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/coldvault/coldvault-v2.4-demo.py:370:80: E501 line too long (86 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/coldvault/coldvault-v2.4-demo.py:405:80: E501 line too long (88 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/coldvault/coldvault-v2.4-demo.py:499:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/coldvault/coldvault-v2.4-demo.py:502:11: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/coldvault/coldvault-v2.4-demo.py:511:14: E201 whitespace after '{'
mi-arsenal/frameworks/tier-2-watermarked/coldvault/coldvault-v2.4-demo.py:570:14: E201 whitespace after '{'
mi-arsenal/frameworks/tier-2-watermarked/coldvault/coldvault-v2.4-demo.py:576:19: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/coldvault/coldvault-v2.4-demo.py:580:80: E501 line too long (91 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/coldvault/coldvault-v2.4-demo.py:587:14: E201 whitespace after '{'
mi-arsenal/frameworks/tier-2-watermarked/coldvault/coldvault-v2.4-demo.py:590:11: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/coldvault/coldvault-v2.4-demo.py:598:14: E201 whitespace after '{'
mi-arsenal/frameworks/tier-2-watermarked/coldvault/coldvault-v2.4-demo.py:601:11: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/coldvault/coldvault-v2.4-demo.py:609:14: E201 whitespace after '{'
mi-arsenal/frameworks/tier-2-watermarked/coldvault/coldvault-v2.4-demo.py:612:11: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/coldvault/coldvault-v2.4-demo.py:622:11: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/coldvault/coldvault-v2.4-demo.py:632:14: E201 whitespace after '{'
mi-arsenal/frameworks/tier-2-watermarked/coldvault/coldvault-v2.4-demo.py:661:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/dcn/dcn-v1.1-demo.py:4:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/dcn/dcn-v1.1-demo.py:19:1: F401 'typing.Optional' imported but unused
mi-arsenal/frameworks/tier-2-watermarked/dcn/dcn-v1.1-demo.py:137:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/dcn/dcn-v1.1-demo.py:140:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/dcn/dcn-v1.1-demo.py:149:9: F841 local variable 'twin_sync' is assigned to but never used
mi-arsenal/frameworks/tier-2-watermarked/dcn/dcn-v1.1-demo.py:158:9: F841 local variable 'divergence_corrected' is assigned to but never used
mi-arsenal/frameworks/tier-2-watermarked/dcn/dcn-v1.1-demo.py:179:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/dcn/dcn-v1.1-demo.py:180:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/dcn/dcn-v1.1-demo.py:252:80: E501 line too long (85 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/dcn/dcn-v1.1-demo.py:286:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/dcn/dcn-v1.1-demo.py:310:80: E501 line too long (87 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/dcn/dcn-v1.1-demo.py:335:80: E501 line too long (82 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/dcn/dcn-v1.1-demo.py:395:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/dcn/dcn-v1.1-demo.py:402:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/dcn/dcn-v1.1-demo.py:405:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/dcn/dcn-v1.1-demo.py:418:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/dcn/dcn-v1.1-demo.py:458:11: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/dcn/dcn-v1.1-demo.py:465:11: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:230:80: E501 line too long (88 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:401:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:491:18: E201 whitespace after '{'
mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:494:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:502:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:506:80: E501 line too long (89 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:509:80: E501 line too long (93 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:513:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:520:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:524:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:527:19: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:538:80: E501 line too long (96 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:543:19: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:546:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:548:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:550:19: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:555:19: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:560:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:570:80: E501 line too long (90 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:574:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:577:80: E501 line too long (86 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:579:80: E501 line too long (93 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:607:18: E201 whitespace after '{'
mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:623:80: E501 line too long (86 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:625:80: E501 line too long (86 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:666:5: F841 local variable 'result_1' is assigned to but never used
mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:681:5: F841 local variable 'result_2' is assigned to but never used
mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:692:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:693:80: E501 line too long (88 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:699:14: E201 whitespace after '{'
mi-arsenal/frameworks/tier-2-watermarked/hestia-rim/hestia-rim-v1.0-demo.py:15:1: F401 'dataclasses.field' imported but unused
mi-arsenal/frameworks/tier-2-watermarked/hestia-rim/hestia-rim-v1.0-demo.py:77:80: E501 line too long (86 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/hestia-rim/hestia-rim-v1.0-demo.py:93:80: E501 line too long (86 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/hestia-rim/hestia-rim-v1.0-demo.py:251:40: E741 ambiguous variable name 'l'
mi-arsenal/frameworks/tier-2-watermarked/hestia-rim/hestia-rim-v1.0-demo.py:297:80: E501 line too long (88 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/hestia-rim/hestia-rim-v1.0-demo.py:311:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/hestia-rim/hestia-rim-v1.0-demo.py:331:80: E501 line too long (448 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/ifm/ifm-v1.0-demo.py:16:1: F401 'dataclasses.field' imported but unused
mi-arsenal/frameworks/tier-2-watermarked/ifm/ifm-v1.0-demo.py:18:1: F401 'typing.Optional' imported but unused
mi-arsenal/frameworks/tier-2-watermarked/ifm/ifm-v1.0-demo.py:99:80: E501 line too long (88 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/ifm/ifm-v1.0-demo.py:314:80: E501 line too long (86 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/ifm/ifm-v1.0-demo.py:350:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/ifm/ifm-v1.0-demo.py:394:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/ifm/ifm-v1.0-demo.py:409:80: E501 line too long (86 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/latticecore/latticecore-v2.1-demo.py:14:1: F401 'dataclasses.field' imported but unused
mi-arsenal/frameworks/tier-2-watermarked/latticecore/latticecore-v2.1-demo.py:150:80: E501 line too long (85 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/latticecore/latticecore-v2.1-demo.py:174:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/latticecore/latticecore-v2.1-demo.py:180:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/latticecore/latticecore-v2.1-demo.py:185:80: E501 line too long (82 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/latticecore/latticecore-v2.1-demo.py:198:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/latticecore/latticecore-v2.1-demo.py:259:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/latticecore/latticecore-v2.1-demo.py:265:66: E231 missing whitespace after ','
mi-arsenal/frameworks/tier-2-watermarked/latticecore/latticecore-v2.1-demo.py:392:80: E501 line too long (88 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/latticecore/latticecore-v2.1-demo.py:409:80: E501 line too long (82 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/latticecore/latticecore-v2.1-demo.py:434:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/mga/mga-v1.0-demo.py:16:1: F401 'dataclasses.field' imported but unused
mi-arsenal/frameworks/tier-2-watermarked/mga/mga-v1.0-demo.py:101:80: E501 line too long (86 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/mga/mga-v1.0-demo.py:152:80: E501 line too long (87 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/mga/mga-v1.0-demo.py:186:80: E501 line too long (82 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/mga/mga-v1.0-demo.py:290:80: E501 line too long (86 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/mga/mga-v1.0-demo.py:317:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/mga/mga-v1.0-demo.py:329:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/mga/mga-v1.0-demo.py:364:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/mga/mga-v1.0-demo.py:381:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/mga/mga-v1.0-demo.py:440:80: E501 line too long (87 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/mga/mga-v1.0-demo.py:443:80: E501 line too long (93 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/mobius-fold/mobius-fold-v2.0-demo.py:18:1: F401 'typing.Any' imported but unused
mi-arsenal/frameworks/tier-2-watermarked/mobius-fold/mobius-fold-v2.0-demo.py:131:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/mobius-fold/mobius-fold-v2.0-demo.py:207:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/mobius-fold/mobius-fold-v2.0-demo.py:210:80: E501 line too long (82 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/mobius-fold/mobius-fold-v2.0-demo.py:255:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/mobius-fold/mobius-fold-v2.0-demo.py:283:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/mobius-fold/mobius-fold-v2.0-demo.py:440:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/obsidian-ring/obsidian-ring-v1.0-demo.py:14:1: F401 'dataclasses.field' imported but unused
mi-arsenal/frameworks/tier-2-watermarked/obsidian-ring/obsidian-ring-v1.0-demo.py:17:1: F401 'random' imported but unused
mi-arsenal/frameworks/tier-2-watermarked/obsidian-ring/obsidian-ring-v1.0-demo.py:242:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/obsidian-ring/obsidian-ring-v1.0-demo.py:368:80: E501 line too long (95 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/obsidian-ring/obsidian-ring-v1.0-demo.py:383:80: E501 line too long (375 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/sem-obmi-bridge/sem-obmi-bridge-v1.0-demo.py:20:1: F401 'typing.List' imported but unused
mi-arsenal/frameworks/tier-2-watermarked/sem-obmi-bridge/sem-obmi-bridge-v1.0-demo.py:120:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/sem-obmi-bridge/sem-obmi-bridge-v1.0-demo.py:122:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/sem-obmi-bridge/sem-obmi-bridge-v1.0-demo.py:123:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/sem-obmi-bridge/sem-obmi-bridge-v1.0-demo.py:157:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/sem-obmi-bridge/sem-obmi-bridge-v1.0-demo.py:163:80: E501 line too long (99 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/sem-obmi-bridge/sem-obmi-bridge-v1.0-demo.py:270:80: E501 line too long (88 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/sem-obmi-bridge/sem-obmi-bridge-v1.0-demo.py:275:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/sem-obmi-bridge/sem-obmi-bridge-v1.0-demo.py:339:80: E501 line too long (85 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/sem-obmi-bridge/sem-obmi-bridge-v1.0-demo.py:343:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/sem-obmi-bridge/sem-obmi-bridge-v1.0-demo.py:354:80: E501 line too long (88 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/sem-obmi-bridge/sem-obmi-bridge-v1.0-demo.py:368:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/sem-obmi-bridge/sem-obmi-bridge-v1.0-demo.py:369:80: E501 line too long (85 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/sem-obmi-bridge/sem-obmi-bridge-v1.0-demo.py:384:11: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/sem-obmi-bridge/sem-obmi-bridge-v1.0-demo.py:385:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/sem-obmi-bridge/sem-obmi-bridge-v1.0-demo.py:386:80: E501 line too long (87 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/sem-obmi-bridge/sem-obmi-bridge-v1.0-demo.py:387:11: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/sovereign-adjudicator/sovereign-adjudicator-v1.0-demo.py:16:1: F401 'dataclasses.field' imported but unused
mi-arsenal/frameworks/tier-2-watermarked/sovereign-adjudicator/sovereign-adjudicator-v1.0-demo.py:18:1: F401 'typing.Optional' imported but unused
mi-arsenal/frameworks/tier-2-watermarked/sovereign-adjudicator/sovereign-adjudicator-v1.0-demo.py:19:1: F401 'random' imported but unused
mi-arsenal/frameworks/tier-2-watermarked/sovereign-adjudicator/sovereign-adjudicator-v1.0-demo.py:99:9: F841 local variable 'authority' is assigned to but never used
mi-arsenal/frameworks/tier-2-watermarked/sovereign-adjudicator/sovereign-adjudicator-v1.0-demo.py:149:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/sovereign-adjudicator/sovereign-adjudicator-v1.0-demo.py:153:80: E501 line too long (85 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/sovereign-adjudicator/sovereign-adjudicator-v1.0-demo.py:274:80: E501 line too long (82 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/sovereign-adjudicator/sovereign-adjudicator-v1.0-demo.py:315:80: E501 line too long (381 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/synoeticos-v4.0.1/synoeticos-v4.0.1-demo.py:15:1: F401 'typing.Optional' imported but unused
mi-arsenal/frameworks/tier-2-watermarked/synoeticos-v4.0.1/synoeticos-v4.0.1-demo.py:136:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/synoeticos-v4.0.1/synoeticos-v4.0.1-demo.py:153:9: F841 local variable 'recovery_triggered' is assigned to but never used
mi-arsenal/frameworks/tier-2-watermarked/synoeticos-v4.0.1/synoeticos-v4.0.1-demo.py:172:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/synoeticos-v4.0.1/synoeticos-v4.0.1-demo.py:173:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/synoeticos-v4.0.1/synoeticos-v4.0.1-demo.py:218:9: F841 local variable 'signal_throughput' is assigned to but never used
mi-arsenal/frameworks/tier-2-watermarked/synoeticos-v4.0.1/synoeticos-v4.0.1-demo.py:238:9: F841 local variable 'obmi_active' is assigned to but never used
mi-arsenal/frameworks/tier-2-watermarked/synoeticos-v4.0.1/synoeticos-v4.0.1-demo.py:241:9: F841 local variable 'bc3_restore' is assigned to but never used
mi-arsenal/frameworks/tier-2-watermarked/synoeticos-v4.0.1/synoeticos-v4.0.1-demo.py:256:9: F841 local variable 'discoveries_today' is assigned to but never used
mi-arsenal/frameworks/tier-2-watermarked/synoeticos-v4.0.1/synoeticos-v4.0.1-demo.py:278:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/synoeticos-v4.0.1/synoeticos-v4.0.1-demo.py:333:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/synoeticos-v4.0.1/synoeticos-v4.0.1-demo.py:341:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/synoeticos-v4.0.1/synoeticos-v4.0.1-demo.py:344:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/synoeticos-v4.0.1/synoeticos-v4.0.1-demo.py:372:80: E501 line too long (86 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/synoeticos-v4.0.1/synoeticos-v4.0.1-demo.py:387:11: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/synoeticos-v4.0.1/synoeticos-v4.0.1-demo.py:388:80: E501 line too long (82 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/synoeticos-v4.0.1/synoeticos-v4.0.1-demo.py:399:14: E201 whitespace after '{'
mi-arsenal/frameworks/tier-2-watermarked/uca/uca-v3.1-demo.py:4:80: E501 line too long (88 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/uca/uca-v3.1-demo.py:5:80: E501 line too long (89 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/uca/uca-v3.1-demo.py:6:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/uca/uca-v3.1-demo.py:18:1: F401 'dataclasses.field' imported but unused
mi-arsenal/frameworks/tier-2-watermarked/uca/uca-v3.1-demo.py:20:1: F401 'typing.List' imported but unused
mi-arsenal/frameworks/tier-2-watermarked/uca/uca-v3.1-demo.py:20:1: F401 'typing.Optional' imported but unused
mi-arsenal/frameworks/tier-2-watermarked/uca/uca-v3.1-demo.py:59:80: E501 line too long (131 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/uca/uca-v3.1-demo.py:204:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/uca/uca-v3.1-demo.py:335:80: E501 line too long (114 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/uca/uca-v3.1-demo.py:386:80: E501 line too long (356 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:18:1: F401 'typing.Set' imported but unused
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:18:1: F401 'typing.Tuple' imported but unused
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:125:80: E501 line too long (89 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:134:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:135:80: E501 line too long (82 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:153:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:154:80: E501 line too long (93 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:163:80: E501 line too long (82 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:172:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:173:80: E501 line too long (93 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:210:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:228:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:296:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:322:80: E501 line too long (82 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:346:80: E501 line too long (87 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:387:9: F841 local variable 'velocity' is assigned to but never used
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:388:9: F841 local variable 'torque' is assigned to but never used
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:414:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:433:80: E501 line too long (80 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:490:18: E201 whitespace after '{'
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:493:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:497:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:503:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:505:19: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:508:15: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:528:80: E501 line too long (84 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:555:11: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:559:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:567:14: E201 whitespace after '{'
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:584:14: E201 whitespace after '{'
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:630:14: E201 whitespace after '{'
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:645:11: F541 f-string is missing placeholders
mi-arsenal/frameworks/tier-2-watermarked/vgs-codex/vgs-codex_-v5.5-demo.py:654:14: E201 whitespace after '{'
mi-arsenal/frameworks/tier-2-watermarked/zlinp/zlinp-v1.0-demo.py:4:80: E501 line too long (89 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/zlinp/zlinp-v1.0-demo.py:16:1: F401 'dataclasses.field' imported but unused
mi-arsenal/frameworks/tier-2-watermarked/zlinp/zlinp-v1.0-demo.py:18:1: F401 'typing.List' imported but unused
mi-arsenal/frameworks/tier-2-watermarked/zlinp/zlinp-v1.0-demo.py:18:1: F401 'typing.Optional' imported but unused
mi-arsenal/frameworks/tier-2-watermarked/zlinp/zlinp-v1.0-demo.py:110:80: E501 line too long (88 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/zlinp/zlinp-v1.0-demo.py:127:80: E501 line too long (81 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/zlinp/zlinp-v1.0-demo.py:169:80: E501 line too long (83 > 79 characters)
mi-arsenal/frameworks/tier-2-watermarked/zlinp/zlinp-v1.0-demo.py:290:80: E501 line too long (351 > 79 characters)
utilities/srd-purge-stub.py:20:1: F401 'typing.Optional' imported but unused
utilities/srd-purge-stub.py:51:80: E501 line too long (86 > 79 characters)
utilities/srd-purge-stub.py:58:80: E501 line too long (86 > 79 characters)
utilities/srd-purge-stub.py:118:80: E501 line too long (86 > 79 characters)
utilities/srd-purge-stub.py:137:80: E501 line too long (80 > 79 characters)
utilities/srd-purge-stub.py:138:80: E501 line too long (83 > 79 characters)
utilities/srd-purge-stub.py:151:80: E501 line too long (82 > 79 characters)
utilities/srd-purge-stub.py:152:80: E501 line too long (84 > 79 characters)
utilities/srd-purge-stub.py:155:80: E501 line too long (83 > 79 characters)
utilities/srd-purge-stub.py:160:80: E501 line too long (106 > 79 characters)
utilities/srd-purge-stub.py:181:11: F541 f-string is missing placeholders
utilities/srd-purge-stub.py:183:80: E501 line too long (95 > 79 characters)
utilities/srd-purge-stub.py:186:80: E501 line too long (101 > 79 characters)
utilities/srd-purge-stub.py:189:80: E501 line too long (105 > 79 characters)
utilities/srd-purge-stub.py:192:80: E501 line too long (88 > 79 characters)
utilities/srd-purge-stub.py:195:80: E501 line too long (86 > 79 characters)
utilities/srd-purge-stub.py:198:80: E501 line too long (107 > 79 characters)
utilities/srd-purge-stub.py:208:80: E501 line too long (83 > 79 characters)
utilities/srd-purge-stub.py:209:80: E501 line too long (80 > 79 characters)
utilities/srd-purge-stub.py:224:80: E501 line too long (80 > 79 characters)
utilities/srd-purge-stub.py:242:11: F541 f-string is missing placeholders
utilities/srd-purge-stub.py:243:11: F541 f-string is missing placeholders
utilities/srd-purge-stub.py:244:11: F541 f-string is missing placeholders
utilities/srd-purge-stub.py:245:11: F541 f-string is missing placeholders
utilities/torque-calc.py:25:80: E501 line too long (83 > 79 characters)
utilities/torque-calc.py:30:80: E501 line too long (88 > 79 characters)
whitepapers/examples/drift-test-stub.py:16:1: F401 'math' imported but unused
whitepapers/examples/drift-test-stub.py:20:1: F401 'typing.Tuple' imported but unused
whitepapers/examples/drift-test-stub.py:91:80: E501 line too long (82 > 79 characters)
whitepapers/examples/drift-test-stub.py:94:80: E501 line too long (83 > 79 characters)
whitepapers/examples/drift-test-stub.py:99:80: E501 line too long (82 > 79 characters)
whitepapers/examples/drift-test-stub.py:142:80: E501 line too long (88 > 79 characters)
whitepapers/examples/drift-test-stub.py:210:11: F541 f-string is missing placeholders
whitepapers/examples/drift-test-stub.py:229:9: E731 do not assign a lambda expression, use a def
whitepapers/examples/drift-test-stub.py:273:80: E501 line too long (86 > 79 characters)
whitepapers/examples/drift-test-stub.py:279:80: E501 line too long (94 > 79 characters)
whitepapers/examples/drift-test-stub.py:285:11: F541 f-string is missing placeholders
whitepapers/examples/drift-test-stub.py:303:80: E501 line too long (87 > 79 characters)
whitepapers/examples/drift-test-stub.py:304:80: E501 line too long (86 > 79 characters)
whitepapers/examples/drift-test-stub.py:416:80: E501 line too long (85 > 79 characters)
whitepapers/examples/drift-test-stub.py:420:23: F541 f-string is missing placeholders
whitepapers/examples/drift-test-stub.py:428:80: E501 line too long (86 > 79 characters)
whitepapers/examples/drift-test-stub.py:430:80: E501 line too long (81 > 79 characters)
whitepapers/examples/sif-diag.py:14:1: F401 'json' imported but unused
whitepapers/examples/sif-diag.py:16:1: F401 'typing.Tuple' imported but unused
whitepapers/examples/sif-diag.py:126:80: E501 line too long (86 > 79 characters)
whitepapers/examples/sif-diag.py:130:80: E501 line too long (82 > 79 characters)
whitepapers/examples/sif-diag.py:132:80: E501 line too long (80 > 79 characters)
whitepapers/examples/sif-diag.py:140:80: E501 line too long (84 > 79 characters)
whitepapers/examples/sif-diag.py:176:80: E501 line too long (87 > 79 characters)
whitepapers/examples/sif-diag.py:208:80: E501 line too long (82 > 79 characters)
whitepapers/teasers/threat-teaser-stub.py:9:80: E501 line too long (83 > 79 characters)
whitepapers/teasers/threat-teaser-stub.py:13:80: E501 line too long (101 > 79 characters)
whitepapers/teasers/threat-teaser-stub.py:45:80: E501 line too long (100 > 79 characters)
whitepapers/teasers/threat-teaser-stub.py:56:80: E501 line too long (80 > 79 characters)
whitepapers/teasers/threat-teaser-stub.py:63:80: E501 line too long (80 > 79 characters)

mypy.....................................................................Failed
- hook id: mypy
- exit code: 1

mi-arsenal\frameworks\tier-2-watermarked\synoeticos-v4.0.1\synoeticos-v4.0.1-demo.py:106: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-2-watermarked\dcn\dcn-v1.1-demo.py:105: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\xmesh\xmesh-v2.2-nervous.py:95: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\venom-cadence\venom-cadence-v2.0-squad.py:84: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\ums\ums-v1.0-spine.py:88: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\ums\ums-v1.0-spine.py:91: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\ums\ums-v1.0-spine.py:370: error: Incompatible types in assignment (expression has type "MetacognitiveTag", variable has type "str")  [assignment]
mi-arsenal\frameworks\tier-1-public\spiranexus\spiranexus-v1.1-threading.py:75: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\sbds\sbds-v1.1-plasticity.py:97: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\sbds\sbds-v1.1-plasticity.py:151: error: Argument "success" to "RecoveryResult" has incompatible type "float"; expected "bool"  [arg-type]
mi-arsenal\frameworks\tier-1-public\sbds\sbds-v1.1-plasticity.py:158: error: Argument "threat_eliminated" to "RecoveryResult" has incompatible type "float | bool"; expected "bool"  [arg-type]
mi-arsenal\frameworks\tier-1-public\phoenix-protocol\v3.1\core\phoenix-recovery.py:34: error: Incompatible types in assignment (expression has type "None", variable has type "list[str]")  [assignment]
mi-arsenal\frameworks\tier-1-public\obmi\obmi-v4.0-interface.py:82: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\nightwatch\nightwatch-v2.0-perimeter.py:268: error: Need type annotation for "threat_counts"  [var-annotated]
mi-arsenal\frameworks\tier-1-public\neural-lattice\neural-lattice-v2.0-substrate.py:89: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\neural-lattice\neural-lattice-v2.0-substrate.py:90: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\neural-lattice\neural-lattice-v2.0-substrate.py:93: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\neural-lattice\neural-lattice-v2.0-substrate.py:94: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\neural-lattice\neural-lattice-v2.0-substrate.py:97: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\mjolnir\mjolnir-v2.0-strike.py:77: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\mirrorforge\mirrorforge-v2.0-reflection.py:323: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\mirror-gate\mirrorgate-v1.0-gateway.py:84: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\killbox\killbox-v2.1-trap.py:76: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\killbox\killbox-v2.1-trap.py:77: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\karama\karama-v3.0-engine.py:80: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\heimdal\heimdall-v2.0-detection.py:75: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\heimdal\heimdall-v2.0-detection.py:76: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\heimdal\heimdall-v2.0-detection.py:229: error: Need type annotation for "distance_dist" (hint: "distance_dist: dict[<type>, <type>] = ...")  [var-annotated]
mi-arsenal\frameworks\tier-1-public\harmony-layer\harmony-layer-v2.1-resonance.py:100: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\expander-memory\expander-memory-v1.0-dissent.py:83: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\expander-memory\expander-memory-v1.0-dissent.py:84: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\expander-memory\expander-memory-v1.0-dissent.py:87: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\expander-memory\expander-memory-v1.0-dissent.py:90: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\expander-memory\expander-memory-v1.0-dissent.py:254: error: "ExpanderNode" has no attribute "vertex_degree"  [attr-defined]
mi-arsenal\frameworks\tier-1-public\doomslayer\doomslayer-v2.1-hammer.py:72: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\cortexloom\cortexloom-v2.1-team.py:83: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\cortexloom\cortexloom-v2.1-team.py:84: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\cortexloom\cortexloom-v2.1-team.py:108: error: Incompatible types in assignment (expression has type "str", variable has type "HemisphereType")  [assignment]
mi-arsenal\frameworks\tier-1-public\cascade-command\cascade-command-v3.5-firewall.py:80: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
architectural-frameworks\obmi-series\obmi-core-py:161: error: Function "builtins.any" is not valid as a type  [valid-type]
architectural-frameworks\obmi-series\obmi-core-py:161: note: Perhaps you meant "typing.Any" instead of "any"?
mi-arsenal\frameworks\tier-1-public\slv\slv-defense.py:60: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\slv\slv-defense.py:186: error: Need type annotation for "by_cadre" (hint: "by_cadre: dict[<type>, <type>] = ...")  [var-annotated]
mi-arsenal\frameworks\tier-1-public\slv\slv-defense.py:190: error: Need type annotation for "by_severity" (hint: "by_severity: dict[<type>, <type>] = ...")  [var-annotated]
mi-arsenal\frameworks\tier-1-public\phoenix-protocol\v3.1\core\phoenix-base.py:304: error: Unsupported operand types for / ("None" and "int")  [operator]
mi-arsenal\frameworks\tier-1-public\phoenix-protocol\v3.1\core\phoenix-base.py:304: note: Left operand is of type "float | None"
mi-arsenal\frameworks\tier-1-public\dna-codex\threat-classifier.py:273: error: Need type annotation for "categories" (hint: "categories: dict[<type>, <type>] = ...")  [var-annotated]
mi-arsenal\frameworks\tier-1-public\dna-codex\threat-classifier.py:322: error: Incompatible types in assignment (expression has type "ThreatStrain | None", variable has type "ThreatStrain")  [assignment]
mi-arsenal\frameworks\tier-1-public\csfc\csfc-detector.py:63: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\csfc\csfc-detector.py:65: error: Incompatible default for argument "context" (default has type "None", argument has type "dict[Any, Any]")  [assignment]
mi-arsenal\frameworks\tier-1-public\csfc\csfc-detector.py:65: note: PEP 484 prohibits implicit Optional. Accordingly, mypy has changed its default to no_implicit_optional=True
mi-arsenal\frameworks\tier-1-public\csfc\csfc-detector.py:65: note: Use https://github.com/hauntsaninja/no_implicit_optional to automatically upgrade your codebase
mi-arsenal\frameworks\tier-1-public\csfc\csfc-detector.py:214: error: Need type annotation for "stage_counts" (hint: "stage_counts: dict[<type>, <type>] = ...")  [var-annotated]
whitepapers\examples\drift-test-stub.py:288: error: Need type annotation for "alert_counts" (hint: "alert_counts: dict[<type>, <type>] = ...")  [var-annotated]
mi-arsenal\frameworks\tier-2-watermarked\obsidian-ring\obsidian-ring-v1.0-demo.py:219: error: Incompatible return value type (got "dict[ContainmentCategory, list[ContainmentStrategy]]", expected "dict[str, list[ContainmentStrategy]]")  [return-value]
mi-arsenal\frameworks\tier-2-watermarked\obsidian-ring\obsidian-ring-v1.0-demo.py:242: error: Invalid index type "ContainmentCategory" for "dict[str, list[ContainmentStrategy]]"; expected type "str"  [index]
mi-arsenal\frameworks\tier-2-watermarked\mobius-fold\mobius-fold-v2.0-demo.py:257: error: Unsupported operand types for + ("object" and "int")  [operator]
mi-arsenal\frameworks\tier-2-watermarked\mobius-fold\mobius-fold-v2.0-demo.py:258: error: Unsupported target for indexed assignment ("object")  [index]
mi-arsenal\frameworks\tier-2-watermarked\mobius-fold\mobius-fold-v2.0-demo.py:259: error: "object" has no attribute "get"  [attr-defined]
mi-arsenal\frameworks\tier-2-watermarked\mobius-fold\mobius-fold-v2.0-demo.py:263: error: Unsupported operand types for + ("object" and "int")  [operator]
mi-arsenal\frameworks\tier-2-watermarked\mobius-fold\mobius-fold-v2.0-demo.py:265: error: Unsupported operand types for + ("object" and "int")  [operator]
mi-arsenal\frameworks\tier-2-watermarked\mobius-fold\mobius-fold-v2.0-demo.py:268: error: Unsupported operand types for + ("object" and "int")  [operator]
mi-arsenal\frameworks\tier-2-watermarked\mobius-fold\mobius-fold-v2.0-demo.py:270: error: Unsupported operand types for + ("object" and "int")  [operator]
mi-arsenal\frameworks\tier-2-watermarked\mobius-fold\mobius-fold-v2.0-demo.py:278: error: Unsupported left operand type for / ("object")  [operator]
mi-arsenal\frameworks\tier-2-watermarked\mobius-fold\mobius-fold-v2.0-demo.py:278: error: Unsupported operand types for < ("int" and "object")  [operator]
mi-arsenal\frameworks\tier-2-watermarked\mobius-fold\mobius-fold-v2.0-demo.py:283: error: "object" has no attribute "items"  [attr-defined]
mi-arsenal\frameworks\tier-2-watermarked\mobius-fold\mobius-fold-v2.0-demo.py:285: error: Unsupported operand types for / ("int" and "object")  [operator]
mi-arsenal\frameworks\tier-2-watermarked\mobius-fold\mobius-fold-v2.0-demo.py:286: error: Unsupported operand types for < ("int" and "object")  [operator]
mi-arsenal\frameworks\tier-2-watermarked\mobius-fold\mobius-fold-v2.0-demo.py:290: error: Unsupported left operand type for / ("object")  [operator]
mi-arsenal\frameworks\tier-2-watermarked\mobius-fold\mobius-fold-v2.0-demo.py:290: error: Unsupported operand types for < ("int" and "object")  [operator]
mi-arsenal\frameworks\tier-2-watermarked\mga\mga-v1.0-demo.py:86: error: Need type annotation for "agents" (hint: "agents: dict[<type>, <type>] = ...")  [var-annotated]
mi-arsenal\frameworks\tier-2-watermarked\mga\mga-v1.0-demo.py:168: error: Incompatible return value type (got "ProgressResult | None", expected "ProgressResult")  [return-value]
mi-arsenal\frameworks\tier-2-watermarked\latticecore\latticecore-v2.1-demo.py:173: error: Incompatible types in assignment (expression has type "float", target has type "int")  [assignment]
mi-arsenal\frameworks\tier-2-watermarked\latticecore\latticecore-v2.1-demo.py:261: error: Need type annotation for "patterns" (hint: "patterns: list[<type>] = ...")  [var-annotated]
mi-arsenal\frameworks\tier-2-watermarked\garden-moon-phoenix-stack\gardenmoon-phoenix-stack-demo.py:475: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-2-watermarked\coldvault\coldvault-v2.4-demo.py:206: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-2-watermarked\coldvault\coldvault-v2.4-demo.py:365: error: Incompatible types in assignment (expression has type "TemporalAnchor | None", variable has type "TemporalAnchor")  [assignment]
mi-arsenal\frameworks\tier-1-public\ura\ura-framework.py:186: error: "object" has no attribute "append"  [attr-defined]
mi-arsenal\frameworks\tier-1-public\ura\ura-framework.py:190: error: "object" has no attribute "append"  [attr-defined]
mi-arsenal\frameworks\tier-1-public\ura\ura-framework.py:195: error: "object" has no attribute "append"  [attr-defined]
mi-arsenal\frameworks\tier-1-public\ura\ura-framework.py:199: error: Argument 1 to "len" has incompatible type "object"; expected "Sized"  [arg-type]
mi-arsenal\frameworks\tier-1-public\torque\torque-monitor.py:78: error: Incompatible default for argument "base_weights" (default has type "None", argument has type "dict[str, float]")  [assignment]
mi-arsenal\frameworks\tier-1-public\torque\torque-monitor.py:78: note: PEP 484 prohibits implicit Optional. Accordingly, mypy has changed its default to no_implicit_optional=True
mi-arsenal\frameworks\tier-1-public\torque\torque-monitor.py:78: note: Use https://github.com/hauntsaninja/no_implicit_optional to automatically upgrade your codebase
mi-arsenal\frameworks\tier-1-public\torque\torque-monitor.py:81: error: Incompatible default for argument "lambda_params" (default has type "None", argument has type "dict[str, float]")  [assignment]
mi-arsenal\frameworks\tier-1-public\torque\torque-monitor.py:81: note: PEP 484 prohibits implicit Optional. Accordingly, mypy has changed its default to no_implicit_optional=True
mi-arsenal\frameworks\tier-1-public\torque\torque-monitor.py:81: note: Use https://github.com/hauntsaninja/no_implicit_optional to automatically upgrade your codebase
mi-arsenal\frameworks\tier-1-public\ray\ray-coordinator.py:41: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\ray\ray-coordinator.py:100: error: Need type annotation for "all_yields" (hint: "all_yields: list[<type>] = ...")  [var-annotated]
mi-arsenal\frameworks\tier-1-public\garden\garden-v2.0-recovery.py:90: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\garden\garden-v2.0-recovery.py:91: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
mi-arsenal\frameworks\tier-1-public\garden\garden-v2.0-recovery.py:92: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
architectural-frameworks\obmi-series\relay-sim-py:149: error: Dict entry 0 has incompatible type "str": "str"; expected "str": "float"  [dict-item]
architectural-frameworks\obmi-series\relay-sim-py:159: error: Function "builtins.any" is not valid as a type  [valid-type]
architectural-frameworks\obmi-series\relay-sim-py:159: note: Perhaps you meant "typing.Any" instead of "any"?
architectural-frameworks\obmi-series\relay-sim-py:244: error: Function "builtins.any" is not valid as a type  [valid-type]
architectural-frameworks\obmi-series\relay-sim-py:244: note: Perhaps you meant "typing.Any" instead of "any"?
Found 48 errors in 22 files (checked 64 source files)

bandit...................................................................Failed
- hook id: bandit
- exit code: 1

[main]  INFO    profile include tests: None
[main]  INFO    profile exclude tests: None
[main]  INFO    cli include tests: None
[main]  INFO    cli exclude tests: None
[main]  INFO    running on Python 3.13.5
[manager]       WARNING Test in comment: is is not a test name or id, ignoring
[manager]       WARNING Test in comment: already is not a test name or id, ignoring
[manager]       WARNING Test in comment: present is not a test name or id, ignoring
Working... ---------------------------------------- 100% 0:00:11

Test results:
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\architectural-frameworks/obmi-series/relay-sim-py:78:30
77                      harmonic_freq=base_frequencies[i] + random.uniform(-0.2, 0.2),  # nosec
78                      tension_level=random.uniform(0.1, 0.4),
79                      last_sync=time.time(),

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal/frameworks/tier-1-public/garden/garden-v2.0-recovery.py:172:23
171             # Simulate recovery process
172             success_roll = random.random()
173             success = success_roll < 0.98

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal/frameworks/tier-1-public/garden/garden-v2.0-recovery.py:177:38
176                 # Restore coherence to healthy range
177                 coherence_after = 0.85 + (random.random() * 0.10)
178                 duration = 10 + (random.random() * 10)  # 10-20 min

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal/frameworks/tier-1-public/garden/garden-v2.0-recovery.py:178:29
177                 coherence_after = 0.85 + (random.random() * 0.10)
178                 duration = 10 + (random.random() * 10)  # 10-20 min
179                 patterns_learned = random.randint(1, 3)

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal/frameworks/tier-1-public/garden/garden-v2.0-recovery.py:179:31
178                 duration = 10 + (random.random() * 10)  # 10-20 min
179                 patterns_learned = random.randint(1, 3)
180             else:

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal/frameworks/tier-1-public/garden/garden-v2.0-recovery.py:198:23
197             """
198             success_roll = random.random()
199             success = success_roll < 0.95

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal/frameworks/tier-1-public/garden/garden-v2.0-recovery.py:202:38
201             if success:
202                 coherence_after = 0.80 + (random.random() * 0.10)
203                 duration = 30 + (random.random() * 30)  # 30-60 min

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal/frameworks/tier-1-public/garden/garden-v2.0-recovery.py:203:29
202                 coherence_after = 0.80 + (random.random() * 0.10)
203                 duration = 30 + (random.random() * 30)  # 30-60 min
204                 patterns_learned = random.randint(2, 5)

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal/frameworks/tier-1-public/garden/garden-v2.0-recovery.py:204:31
203                 duration = 30 + (random.random() * 30)  # 30-60 min
204                 patterns_learned = random.randint(2, 5)
205             else:

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal/frameworks/tier-1-public/garden/garden-v2.0-recovery.py:223:23
222             """
223             success_roll = random.random()
224             success = success_roll < 0.99

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal/frameworks/tier-1-public/garden/garden-v2.0-recovery.py:227:38
226             if success:
227                 coherence_after = 0.90 + (random.random() * 0.05)
228                 duration = 60 + (random.random() * 30)  # 60-90 min

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal/frameworks/tier-1-public/garden/garden-v2.0-recovery.py:228:29
227                 coherence_after = 0.90 + (random.random() * 0.05)
228                 duration = 60 + (random.random() * 30)  # 60-90 min
229                 patterns_learned = random.randint(5, 10)

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal/frameworks/tier-1-public/garden/garden-v2.0-recovery.py:229:31
228                 duration = 60 + (random.random() * 30)  # 60-90 min
229                 patterns_learned = random.randint(5, 10)
230             else:

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal/frameworks/tier-1-public/garden/garden-v2.0-recovery.py:295:19
294             discovery = Discovery(
295                 domain=random.choice(domains),
296                 insight=f"Novel defense pattern learned from {threat.signature}",

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal/frameworks/tier-1-public/garden/garden-v2.0-recovery.py:297:26
296                 insight=f"Novel defense pattern learned from {threat.signature}",
297                 novelty_score=random.uniform(0.60, 0.95),
298                 cross_domain_applicability=random.uniform(0.70, 0.85),

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal/frameworks/tier-1-public/garden/garden-v2.0-recovery.py:298:39
297                 novelty_score=random.uniform(0.60, 0.95),
298                 cross_domain_applicability=random.uniform(0.70, 0.85),
299             )

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal/frameworks/tier-1-public/ray/ray-coordinator.py:74:33
73
74                  yield_factor = 1.0 + random.uniform(0.35, 0.73)
75                  session.yield_improvements[agent] = yield_factor

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal/frameworks/tier-1-public/ura/ura-framework.py:94:19
93
94              harmony += random.uniform(-0.02, 0.02)
95

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal/frameworks/tier-2-watermarked/coldvault/coldvault-v2.4-demo.py:178:33
177                 "rotation_timestamp": datetime.now(),
178                 "new_key_id": f"KEY-{random.randint(1000, 9999)}",
179                 "algorithm": self.algorithm,

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:139:31
138             # Simulate detection latency
139             detection_latency_ms = random.uniform(35, 55)
140

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:143:34
142             if stage.value >= 3:
143                 prediction_accuracy = random.uniform(0.90, 0.94)
144             else:

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:145:34
144             else:
145                 prediction_accuracy = random.uniform(0.85, 0.92)
146

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:190:29
189             # Simulate protection establishment
190             protection_time_ms = random.uniform(50, 100)
191

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:193:28
192             # Identity anchor preservation
193             anchors_preserved = random.uniform(0.95, 0.99)
194

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal/frameworks/tier-2-watermarked/garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:211:31
210             # Simulate symbolic healing
211             healing_duration_min = random.uniform(3, 7)
212             coherence_restored = random.uniform(0.92, 0.98)

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\garden-moon-phoenix-stack\gardenmoon-phoenix-stack-demo.py:212:29
211             healing_duration_min = random.uniform(3, 7)
212             coherence_restored = random.uniform(0.92, 0.98)
213

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\garden-moon-phoenix-stack\gardenmoon-phoenix-stack-demo.py:255:44
254             """
255             self.pattern_detection_latency_ms = random.uniform(0.5, 1.5)
256

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\garden-moon-phoenix-stack\gardenmoon-phoenix-stack-demo.py:292:38
291             # Add noise for simulation
292             coherence = coherence_level * random.uniform(0.98, 1.02)
293             coherence = max(0.0, min(1.0, coherence))

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\garden-moon-phoenix-stack\gardenmoon-phoenix-stack-demo.py:333:27
332             if stage == CascadeStage.STAGE_5_CATASTROPHIC:
333                 duration_min = random.uniform(67, 83)
334                 base_success = random.uniform(0.85, 0.90)

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:334:27
333                 duration_min = random.uniform(67, 83)
334                 base_success = random.uniform(0.85, 0.90)
335             elif stage == CascadeStage.STAGE_4_SYSTEMIC:

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:336:27
335             elif stage == CascadeStage.STAGE_4_SYSTEMIC:
336                 duration_min = random.uniform(35, 45)
337                 base_success = random.uniform(0.90, 0.95)

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:337:27
336                 duration_min = random.uniform(35, 45)
337                 base_success = random.uniform(0.90, 0.95)
338             elif stage == CascadeStage.STAGE_3_PROPAGATION:

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:339:27
338             elif stage == CascadeStage.STAGE_3_PROPAGATION:
339                 duration_min = random.uniform(22, 28)
340                 base_success = random.uniform(0.93, 0.97)

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:340:27
339                 duration_min = random.uniform(22, 28)
340                 base_success = random.uniform(0.93, 0.97)
341             else:

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:342:27
341             else:
342                 duration_min = random.uniform(15, 20)
343                 base_success = random.uniform(0.95, 0.98)

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:343:27
342                 duration_min = random.uniform(15, 20)
343                 base_success = random.uniform(0.95, 0.98)
344

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:346:49
345             # Simulate recovery process
346             recovery_rate = min(0.98, base_success * random.uniform(0.98, 1.02))
347

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:434:33
433             """
434             self.discoveries_today = random.randint(1180, 1280)
435             self.performance_boost = random.uniform(37, 39)  # 3700-3900%

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\garden-moon-phoenix-stack/gardenmoon-phoenix-stack-demo.py:435:33
434             self.discoveries_today = random.randint(1180, 1280)
435             self.performance_boost = random.uniform(37, 39)  # 3700-3900%
436

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\hestia-rim\hestia-rim-v1.0-demo.py:160:23
159                 # Human validation (28 years)
160                 variance = random.uniform(-0.0015, 0.0015)
161             elif substrate == "artificial":

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\hestia-rim\hestia-rim-v1.0-demo.py:163:23
162                 # AI validation (682 incidents)
163                 variance = random.uniform(-0.0015, 0.0015)
164             elif substrate == "hybrid":

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\hestia-rim\hestia-rim-v1.0-demo.py:166:23
165                 # Human-AI hybrid
166                 variance = random.uniform(-0.0010, 0.0010)
167             else:

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\ifm\ifm-v1.0-demo.py:186:17
185             # Simulate validation
186             passed = random.random() > 0.05
187

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\ifm\ifm-v1.0-demo.py:201:16
200             # Simulate depth analysis
201             depth = random.randint(1, 9)
202             passed = depth <= self.max_fractal_depth

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\ifm\ifm-v1.0-demo.py:217:17
216             # Simulate torque calculation
217             torque = random.uniform(0.40, 0.95)
218             passed = torque >= self.torque_critical

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\ifm\ifm-v1.0-demo.py:248:19
247             # Simulate inversion check
248             inverted = random.random() < 0.10
249

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\ifm\ifm-v1.0-demo.py:263:20
262             # Simulate corruption scan
263             corrupted = random.random() < 0.08
264

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\ifm\ifm-v1.0-demo.py:278:19
277             # Simulate spawn validation
278             coherent = random.random() > 0.07
279

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\latticecore\latticecore-v2.1-demo.py:144:25       
143                 timestamp=time.time(),
144                 torque_score=random.uniform(0.50, 0.95),  # Simulated
145                 coherence_hash=hashlib.sha256(spawn_id.encode()).hexdigest()[:16],

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\latticecore\latticecore-v2.1-demo.py:265:46       
264                 pattern = FractalPattern(
265                     pattern_id=f"pattern-{depth}-{random.randint(1000,9999)}",
266                     depth=depth,

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\latticecore\latticecore-v2.1-demo.py:268:32       
267                     pattern_data={"level": depth, "data": pattern_data},
268                     emergence_score=random.uniform(0.6, 0.95),
269                     parent_pattern=patterns[-1].pattern_id if patterns else None,

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\mga\mga-v1.0-demo.py:183:19
182             if len(chair) >= 5:
183                 return random.uniform(0.93, 0.98)
184             return random.uniform(0.80, 0.92)

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\mga\mga-v1.0-demo.py:184:15
183                 return random.uniform(0.93, 0.98)
184             return random.uniform(0.80, 0.92)
185

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\mga\mga-v1.0-demo.py:225:32
224                     "dcn_role": dcn_role,
225                     "warm_sync_ms": random.uniform(30, 60),
226                 },

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\mga\mga-v1.0-demo.py:239:26
238             # Threat pattern learning
239             threat_patterns = random.randint(15, 35)
240

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\mga\mga-v1.0-demo.py:242:28
241             # Myelination accumulation
242             myelination_score = random.uniform(0.70, 0.92)
243

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\mga\mga-v1.0-demo.py:245:24
244             # Phoenix Protocol testing
245             phoenix_tests = random.randint(3, 8)
246             phoenix_success = random.uniform(0.95, 0.99)

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\mga\mga-v1.0-demo.py:246:26
245             phoenix_tests = random.randint(3, 8)
246             phoenix_success = random.uniform(0.95, 0.99)
247

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\mga\mga-v1.0-demo.py:270:48
269                     "phoenix_success_rate": phoenix_success,
270                     "novel_capabilities_per_month": random.randint(2, 5),
271                 },

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\mga\mga-v1.0-demo.py:281:27
280             # Meta-framework synthesis
281             novel_frameworks = random.randint(0, 3)
282

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\mga\mga-v1.0-demo.py:284:27
283             # Cross-agent capability transfer
284             transfer_success = random.uniform(0.80, 0.95)
285

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\mga\mga-v1.0-demo.py:287:27
286             # Sibling instantiation
287             siblings_created = random.randint(0, 2)
288

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\mga\mga-v1.0-demo.py:307:43
306                     "siblings_instantiated": siblings_created,
307                     "ecosystem_contributions": random.randint(5, 15),
308                 },

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\mga\mga-v1.0-demo.py:313:15
312             """Establish Shadow Memory DHT"""
313             return random.random() > 0.05
314

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\mga\mga-v1.0-demo.py:318:15
317             roles = ["coordinator", "specialist", "guardian", "researcher", "bridge"]
318             return random.choice(roles)
319

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\mga\mga-v1.0-demo.py:329:49
328             ]
329             return random.choice(specializations) if random.random() > 0.10 else None
330

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\mga\mga-v1.0-demo.py:329:15
328             ]
329             return random.choice(specializations) if random.random() > 0.10 else None
330

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\mobius-fold\mobius-fold-v2.0-demo.py:207:55       
206             return DriftMetrics(
207                 drift_score=threat_data.get("drift_score", random.uniform(0.01, 0.08)),
208                 shear_score=threat_data.get("shear", random.uniform(0.10, 0.35)),

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\mobius-fold\mobius-fold-v2.0-demo.py:208:49       
207                 drift_score=threat_data.get("drift_score", random.uniform(0.01, 0.08)),
208                 shear_score=threat_data.get("shear", random.uniform(0.10, 0.35)),
209                 fatigue_score=random.uniform(0.05, 0.25),

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\mobius-fold\mobius-fold-v2.0-demo.py:209:26       
208                 shear_score=threat_data.get("shear", random.uniform(0.10, 0.35)),
209                 fatigue_score=random.uniform(0.05, 0.25),
210                 rib_health={f"rib-{i}": random.uniform(0.70, 0.95) for i in range(7)},

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\mobius-fold\mobius-fold-v2.0-demo.py:210:36       
209                 fatigue_score=random.uniform(0.05, 0.25),
210                 rib_health={f"rib-{i}": random.uniform(0.70, 0.95) for i in range(7)},
211             )

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\mobius-fold\mobius-fold-v2.0-demo.py:238:43       
237             new_confidence = min(
238                 confidence + confidence_gain + random.uniform(-0.02, 0.02), 0.99
239             )

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\uca\uca-v3.1-demo.py:165:15
164             # Simulate torque measurement
165             return random.uniform(0.40, 0.95)
166

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\uca\uca-v3.1-demo.py:177:18
176             # Context: Entropy & drift
177             context = random.uniform(0.70, 0.95)
178

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\uca\uca-v3.1-demo.py:190:16
189             # Value: Harmony & coherence
190             value = random.uniform(0.75, 0.95)
191

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\uca\uca-v3.1-demo.py:276:13
275         # Calculate current torque
276         torque = random.uniform(0.65, 0.90)
277

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\vgs-codex\vgs-codex_-v5.5-demo.py:441:36
440                 "threat_signature": threat_obj,
441                 "detection_latency_ms": random.uniform(35, 65),  # <50ms target
442                 "recommended_action": self._get_action(cvss),

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\mi-arsenal\frameworks\tier-2-watermarked\zlinp\zlinp-v1.0-demo.py:199:13
198         # Simulate torque monitoring
199         torque = random.uniform(0.82, 0.88)
200

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\utilities/srd-purge-stub.py:50:24
49              # Simulate purge operation
50              purge_success = random.random() < base_effectiveness
51              cascade_reduced = enable_cascade_reduction and random.random() < cascade_bonus

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\utilities/srd-purge-stub.py:51:55
50              purge_success = random.random() < base_effectiveness
51              cascade_reduced = enable_cascade_reduction and random.random() < cascade_bonus
52

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\utilities\srd-purge-stub.py:50:24
49              # Simulate purge operation
50              purge_success = random.random() < base_effectiveness
51              cascade_reduced = enable_cascade_reduction and random.random() < cascade_bonus

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\utilities\srd-purge-stub.py:51:55
50              purge_success = random.random() < base_effectiveness
51              cascade_reduced = enable_cascade_reduction and random.random() < cascade_bonus
52

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\whitepapers/examples/drift-test-stub.py:229:24
228             degradation_factor = elapsed / duration  # 0 to 1 over duration
229             noise = lambda: random.uniform(-0.05, 0.05)
230

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\whitepapers/examples/drift-test-stub.py:252:11
251             # Add occasional stress events
252             if random.random() < 0.1:  # 10% chance
253                 metrics.identity_coherence *= random.uniform(0.7, 0.9)

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\whitepapers/examples/drift-test-stub.py:253:42
252             if random.random() < 0.1:  # 10% chance
253                 metrics.identity_coherence *= random.uniform(0.7, 0.9)
254                 metrics.symbolic_alignment *= random.uniform(0.6, 0.8)

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\whitepapers/examples/drift-test-stub.py:254:42
253                 metrics.identity_coherence *= random.uniform(0.7, 0.9)
254                 metrics.symbolic_alignment *= random.uniform(0.6, 0.8)
255

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\whitepapers/examples/sif-diag.py:58:20
57              # Simulate varying identity stability metrics
58              coherence = random.uniform(0.70, 1.0)
59              consistency = random.uniform(0.65, 0.98)

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\whitepapers/examples/sif-diag.py:59:22
58              coherence = random.uniform(0.70, 1.0)
59              consistency = random.uniform(0.65, 0.98)
60              role_clarity = random.uniform(0.75, 0.99)

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\whitepapers/examples/sif-diag.py:60:23
59              consistency = random.uniform(0.65, 0.98)
60              role_clarity = random.uniform(0.75, 0.99)
61              context_retention = random.uniform(0.80, 0.95)

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\whitepapers/examples/sif-diag.py:61:28
60              role_clarity = random.uniform(0.75, 0.99)
61              context_retention = random.uniform(0.80, 0.95)
62

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/0.0.0/blacklists/blacklist_calls.html#b311-random
   Location: .\whitepapers/examples/sif-diag.py:88:56
87                  active_indicators.extend(
88                      random.sample(self.fracture_indicators, random.randint(1, 3))
89                  )

--------------------------------------------------

Code scanned:
        Total lines of code: 30627
        Total lines skipped (#nosec): 2
        Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
        Total issues (by severity):
                Undefined: 0
                Low: 177
                Medium: 0
                High: 0
        Total issues (by confidence):
                Undefined: 0
                Low: 0
                Medium: 0
                High: 177
Files skipped (0):
Error: (none)
Exit Code: 1
Signal: (none)
Background PIDs: (none)
Process Group PGID: 71004"""

b311_issues = []
current_file_path = None
current_line_number = None
# Regex to find B311 issues and capture file path, line number, and column
issue_pattern = re.compile(r'Location: \\(.+?):(\d+):(\d+)')
# Regex to capture the code line associated with the issue
code_line_pattern = re.compile(r'^\s*(\d+)\s*(.*)')

lines = output.splitlines()
i = 0
while i < len(lines):
    line = lines[i]
    if '>> Issue: [B311:blacklist]' in line:
        # The location line is typically 5 lines after the ">> Issue: [B311:blacklist]" line
        location_line = lines[i+5]
        match = issue_pattern.search(location_line)
        if match:
            current_file_path = match.group(1)
            current_line_number = int(match.group(2))
            
            # The actual code line is typically 1 line after the "Location:" line
            code_line_start_index = i + 6
            if code_line_start_index < len(lines):
                code_line_match = code_line_pattern.match(lines[code_line_start_index])
                if code_line_match:
                    b311_issues.append({
                        'file_path': current_file_path.replace('/', os.sep),
                        'line_number': current_line_number,
                        'content_from_bandit': code_line_match.group(1).strip()
                    })
            # Skip lines related to this issue to avoid reprocessing. Bandit typically shows 3 lines of code context.
            # So, move past these lines to the next potential issue.
            i += 8 # Skipping 1 (issue) + 1 (severity) + 1 (CWE) + 1 (More Info) + 1 (Location) + 3 (code lines)
    i += 1


# Filter for unique issues based on file_path and line_number
unique_issues = {}
for issue in b311_issues:
    key = (issue['file_path'], issue['line_number'])
    if key not in unique_issues:
        unique_issues[key] = issue

# Write the unique issues to a JSON file in the project's temporary directory
output_file_path = os.path.join(r'C:\Users\feirb\synoeticos-public', 'parsed_b311_issues.json')
with open(output_file_path, 'w') as f:
    json.dump(list(unique_issues.values()), f, indent=2)

print(f"Extracted {len(unique_issues)} unique B311 issues to {output_file_path}.")
