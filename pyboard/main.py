import lcd160cr
lcd = lcd160cr.LCD160CR('X')
csv = [6703, 12977, 50875, 55133, 55069, 55134, 55134, 53085, 55166, 57247, 55199, 55198, 57247, 59327, 59359, 59359, 57214, 61407, 61375, 61407, 61439, 59294, 59359, 63487, 59327, 57214, 59262, 42458, 44570, 38231, 44602, 57247, 63487, 65535, 65535, 65535, 65535, 55134, 55100, 4226, 4226, 4193, 6370, 6402, 6434, 4289, 4289, 4303, 102, 2081, 6434, 6250, 4194, 10565, 6371, 25651, 19248, 29845, 57311, 27830, 27733, 17201, 19248, 4591, 8785, 48794, 50908, 53052, 51005, 53085, 53053, 55134, 55166, 55167, 55167, 57247, 57279, 57246, 55165, 57279, 57214, 50874, 10603, 2120, 6306, 4233, 6349, 2188, 8494, 4265, 8527, 27634, 27699, 27667, 40344, 44570, 59391, 63487, 65535, 63487, 50972, 65535, 31727, 8452, 2081, 4192, 4258, 4225, 8515, 6402, 6402, 2146, 4239, 10596, 2146, 2147, 6372, 6339, 4259, 23505, 27797, 36248, 23506, 25618, 21393, 19280, 6572, 6736, 8816, 50940, 53020, 53020, 53053, 53085, 53086, 55166, 55166, 55166, 57247, 55134, 59359, 59359, 46590, 23407, 4357, 2180, 6347, 2146, 2117, 6310, 6413, 6348, 4233, 4201, 2113, 2145, 4292, 17003, 25520, 40344, 42489, 61375, 52988, 61407, 65535, 65535, 6403, 4193, 6338, 2080, 2112, 4258, 21162, 4289, 33, 4290, 2113, 8452, 2083, 23570, 8485, 8551, 8485, 17069, 34071, 4586, 27797, 44635, 42522, 6605, 6671, 8752, 40409, 50907, 53020, 53020, 53053, 55101, 55134, 55166, 57214, 55101, 57279, 57246, 4259, 2116, 4232, 12713, 23309, 19082, 10481, 8426, 4259, 8372, 8437, 8470, 8406, 12695, 8435, 4226, 6307, 2113, 2178, 17035, 53053, 50940, 65535, 63487, 65535, 8484, 6274, 4193, 4161, 10369, 2048, 4290, 12710, 4290, 4227, 2086, 2178, 2115, 19377, 8453, 2180, 31989, 4291, 10697, 27797, 34136, 29877, 25684, 2444, 4525, 4623, 6639, 50907, 52988, 50940, 53053, 55101, 55134, 55166, 55133, 57279, 21175, 2152, 2083, 33, 8461, 6349, 2, 34, 34, 35, 34, 2114, 2113, 2114, 2081, 2113, 2081, 4226, 4194, 4226, 32, 65, 2178, 10761, 44601, 63487, 59391, 6372, 4225, 6306, 8353, 6273, 2113, 4322, 4226, 2145, 6342, 2118, 4292, 37, 15022, 36117, 4324, 21424, 6405, 12842, 27765, 25716, 32023, 19345, 67, 6573, 8719, 4591, 15121, 48826, 52956, 50940, 55101, 53020, 55134, 57279, 10611, 2119, 2084, 34, 4228, 2114, 4166, 67, 8429, 6350, 2185, 12653, 2146, 2113, 2113, 4194, 6307, 4226, 4194, 2081, 33, 2145, 19082, 6372, 64, 65, 23470, 46681, 4226, 4226, 10434, 10434, 2081, 2113, 4258, 2145, 6307, 35, 33, 4194, 2, 4280, 10696, 4227, 25684, 4259, 21392, 34103, 27732, 17231, 21425, 2114, 4327, 2379, 4526, 2413, 46714, 50875, 50908, 52988, 57214, 48797, 6417, 4263, 2117, 4232, 10515, 10514, 34, 2082, 4234, 8398, 6319, 6352, 4271, 4303, 4259, 4292, 65, 33, 2113, 2146, 33, 2178, 2146, 2146, 2113, 2178, 13005, 2146, 65, 6339, 6273, 10434, 6273, 2113, 6339, 6371, 4226, 4226, 32, 33, 4259, 12733, 10555, 6372, 66, 6405, 2310, 36249, 10893, 29910, 29877, 15119, 4227, 2147, 4525, 2380, 4558, 6606, 48794, 52956, 57246, 50878, 10611, 2152, 2, 36, 4233, 8465, 2088, 32, 14701, 12658, 2158, 4368, 6549, 8662, 8630, 6513, 8648, 229, 10761, 33, 65, 8550, 132, 2342, 10663, 98, 2146, 164, 2113, 2145, 2113, 6371, 4226, 2080, 2113, 8451, 6370, 4257, 4225, 2145, 2081, 2146, 1, 6317, 6339, 6340, 2147, 19377, 25716, 27764, 32023, 36216, 29910, 4162, 2114, 67, 4491, 4525, 44602, 52956, 57214, 57214, 4262, 2146, 2082, 2085, 8398, 7, 2118, 4266, 4361, 6536, 8598, 2256, 4306, 106, 12597, 72, 8435, 4227, 2146, 2113, 2146, 4259, 4259, 4324, 2114, 4193, 2113, 2145, 25421, 33, 32, 2113, 6339, 64, 4193, 2145, 6402, 4258, 4225, 4225, 2145, 33, 2146, 8497, 4194, 6340, 2149, 2181, 8714, 15151, 17166, 25684, 21425, 15119, 17100, 2114, 2082, 6507, 8716, 55069, 57214, 57214, 4259, 8420, 2113, 2083, 2116, 8399, 29976, 38590, 12728, 12722, 4227, 6316, 6318, 4268, 8496, 4236, 6320, 10643, 4231, 6372, 33873, 6371, 21195, 12678, 16936, 2146, 2146, 4259, 10630, 38131, 27567, 4259, 65, 32, 2210, 4225, 4258, 2145, 4258, 4193, 2145, 2145, 4229, 2145, 6339, 2081, 2082, 10547, 2248, 2180, 19278, 25748, 13037, 27894, 23539, 14987, 2179, 2146, 2147, 50907, 57214, 57214, 14987, 6307, 4193, 2048, 2114, 3, 13115, 30170, 4259, 2147, 2114, 34, 4294, 6506, 8588, 6508, 10735, 8688, 8624, 8526, 6409, 4294, 4260, 66, 8485, 2147, 6372, 6405, 8517, 2179, 23341, 38132, 4226, 12907, 2080, 4322, 2113, 2113, 32, 2113, 2113, 2113, 2080, 33, 2178, 4261, 10508, 16788, 4232, 8462, 4171, 2081, 6339, 15117, 19345, 32056, 19213, 21262, 2146, 2114, 55036, 57182, 57246, 8648, 6307, 2081, 4194, 2082, 8649, 2250, 33, 2146, 4293, 6473, 12847, 15026, 17075, 14994, 17139, 17107, 17140, 19220, 21300, 10699, 6407, 12780, 12813, 10667, 4327, 66, 66, 2146, 34, 131, 8583, 33, 6437, 33, 2080, 32, 32, 2081, 2112, 4258, 2113, 68, 6316, 6282, 4229, 67, 2117, 8430, 2213, 2, 4230, 2211, 6698, 4424, 19346, 21294, 23343, 14890, 2114, 52923, 57182, 8648, 4227, 4226, 2081, 4228, 34, 6405, 4260, 33, 2115, 8554, 19252, 23511, 23478, 23447, 23479, 23479, 21398, 23446, 25591, 19185, 6440, 14861, 17008, 14959, 12750, 8555, 4329, 8620, 17041, 19219, 21268, 19186, 12847, 6506, 33, 0, 0, 32, 32, 2177, 8516, 2113, 1, 33, 4230, 68, 4229, 1, 34, 4261, 14643, 6339, 13231, 6437, 6537, 12943, 25358, 19182, 23343, 2114, 31826, 57214, 19214, 8452, 10532, 8456, 2082, 4227, 2114, 1, 2146, 12780, 21365, 25656, 29818, 27673, 27673, 25624, 27738, 27738, 27737, 27672, 134, 4295, 14959, 19186, 14863, 6475, 2248, 4295, 17073, 19187, 21333, 25559, 25559, 19188, 17009, 8620, 6473, 4294, 0, 0, 2178, 6371, 2145, 4226, 2145, 2113, 2114, 65, 2113, 0, 2081, 6437, 13035, 4291, 6502, 23539, 15185, 21262, 21262, 21230, 19117, 2179, 55101, 99, 42292, 6371, 2183, 65, 1, 2081, 33, 6472, 17139, 21366, 29786, 29883, 29883, 29850, 29818, 29818, 31931, 31930, 25623, 8521, 6441, 17040, 17074, 12783, 2282, 8523, 4327, 10733, 14993, 31931, 29819, 29786, 23448, 19188, 14863, 8619, 8521, 6440, 4293, 0, 4290, 4258, 4258, 6371, 4258, 4258, 4257, 2177, 4193, 6273, 10598, 2177, 10630, 40374, 13006, 32121, 27471, 23310, 21263, 21263, 8551, 6502, 2178, 16904, 8451, 8428, 1, 33, 2114, 2147, 10732, 23445, 27737, 29850, 31963, 31931, 29851, 29851, 31932, 31964, 31931, 27704, 8586, 6440, 14895, 17074, 6444, 17041, 6439, 6474, 10670, 19221, 31899, 31899, 29819, 27673, 21302, 17074, 10636, 10603, 6474, 6409, 4294, 2081, 2080, 32, 32, 2177, 4290, 8450, 10597, 6370, 20964, 12611, 46647, 12840, 10760, 10861, 19444, 25423, 23343, 23311, 21230, 19182, 4325, 2081, 23308, 4226, 2117, 2114, 66, 2082, 2179, 8588, 23510, 27770, 29850, 31963, 29915, 29819, 31931, 31964, 31964, 29851, 25591, 12845, 8553, 10637, 17009, 12880, 4261, 4358, 14895, 10703, 27705, 34077, 31964, 31932, 25593, 23447, 19155, 10669, 8555, 8620, 6474, 8553, 2147, 2113, 32, 2113, 0, 19636, 12971, 8549, 65, 4192, 12643, 6370, 6404, 8617, 12974, 15121, 29584, 25390, 21262, 23311, 21198, 4291, 2081, 6371, 8521, 34, 2146, 2114, 2114, 4261, 19155, 29851, 31996, 31964, 31995, 34108, 34044, 31964, 34044, 34077, 34043, 25591, 10701, 10635, 6475, 8588, 40282, 2179, 99, 17010, 19188, 34044, 31933, 34013, 33981, 27675, 23415, 21268, 12781, 10635, 15057, 14992, 6441, 4359, 13459, 4487, 6470, 2178, 12743, 4226, 2177, 4225, 2145, 4226, 4291, 4454, 10730, 13007, 17267, 31664, 27471, 23343, 23310, 21262, 6372, 65, 6338, 8395, 4260, 2114, 2114, 2146, 4294, 17139, 34076, 31995, 34108, 36189, 36221, 31963, 34141, 36125, 34076, 34044, 27641, 14961, 8556, 8555, 6442, 6409, 8520, 38203, 17043, 25560, 31964, 34045, 34013, 31932, 33948, 27608, 23381, 10669, 8490, 27735, 23477, 10798, 2279, 2179, 2146, 2113, 2113, 36050, 10694, 33937, 33969, 29743, 27598, 25452, 6436, 14924, 15087, 19380, 6307, 27503, 25358, 23342, 21262, 8484, 25421, 6404, 2116, 4292, 2114, 2114, 66, 8586, 23510, 36220, 40414, 40414, 36189, 34109, 36221, 36221, 36156, 36157, 36124, 29818, 25526, 12847, 8556, 6410, 4296, 70, 25526, 27672, 29851, 31964, 31867, 34045, 36092, 33946, 27607, 23347, 10766, 12813, 8620, 12847, 10766, 8619, 2148, 17067, 4226, 10597, 2145, 8451, 4290, 4258, 4225, 4225, 6403, 23372, 10795, 15088, 17268, 29715, 2146, 27471, 23342, 23342, 44438, 12808, 14705, 2147, 8453, 2179, 2114, 66, 8521, 27736, 38334, 36253, 38366, 36221, 34141, 36189, 36189, 36189, 38237, 34012, 29753, 25559, 19187, 10702, 6475, 8587, 10701, 19219, 25527, 27673, 27706, 29851, 29818, 31930, 29785, 21267, 12815, 12782, 10700, 4262, 8620, 10766, 10733, 2246, 2146, 23308, 6404, 4226, 6371, 6339, 4225, 4226, 4258, 4226, 8517, 10828, 17234, 19380, 6307, 33875, 14857, 25455, 23342, 25422, 8484, 38110, 6405, 4292, 2147, 33, 66, 4328, 29849, 36221, 42527, 40414, 38366, 36222, 34141, 36222, 34077, 34044, 31899, 31899, 25527, 23446, 15059, 10735, 12781, 10734, 19218, 23413, 19253, 21366, 17140, 12913, 8590, 8590, 10669, 10669, 10701, 8587, 101, 6539, 8588, 10765, 6506, 99, 2113, 2113, 2081, 4226, 4258, 4258, 4258, 4258, 4258, 8518, 10796, 19347, 19381, 40214, 6340, 23342, 27535, 23310, 12743, 8680, 8554, 2148, 4293, 4260, 34, 2146, 4296, 31995, 40479, 42527, 42559, 42527, 40414, 38366, 36189, 36189, 36156, 31931, 31833, 31833, 29785, 34011, 29818, 25559, 17075, 14962, 17074, 17074, 14994, 14994, 27704, 19188, 12749, 8524, 10636, 10765, 8619, 102, 6474, 8653, 6474, 6571, 4425, 4519, 2081, 2113, 4226, 6338, 4258, 4258, 4225, 4225, 6406, 12942, 19347, 19413, 31859, 35987, 16970, 10598, 25390, 25390, 6731, 130, 12916, 6407, 4293, 2147, 34, 6409, 31962, 42559, 42559, 46751, 44639, 44671, 44639, 40446, 38269, 34076, 34011, 31865, 33913, 36123, 40414, 42527, 42463, 38237, 34012, 23479, 19221, 23478, 23479, 23446, 14961, 16910, 8589, 10701, 10669, 12781, 4232, 10669, 8621, 8652, 6474, 6538, 4326, 2113, 2113, 4193, 6402, 6338, 2145, 4258, 4225, 4359, 12974, 19380, 21461, 36052, 31827, 21228, 29713, 66, 23309, 8550, 8485, 23611, 4325, 6340, 14858, 6374, 2181, 27801, 40479, 44671, 42559, 44671, 46783, 50975, 53087, 36124, 31931, 31865, 33912, 35960, 36090, 38301, 46719, 44606, 46719, 42495, 36157, 34044, 29787, 27641, 25527, 19024, 10539, 8492, 8588, 8588, 12716, 4298, 14897, 10733, 12846, 10765, 8619, 8553, 2178, 2113, 2113, 4290, 4258, 6338, 4225, 6306, 6440, 15056, 19380, 21494, 36019, 31891, 31859, 6404, 33906, 14856, 21098, 4193, 6339, 8457, 2114, 4259, 35, 4261, 25655, 40447, 40446, 42527, 44671, 48831, 55135, 53055, 38301, 29817, 23346, 29587, 31766, 29719, 36155, 40446, 40479, 42527, 46687, 44607, 40383, 40351, 36125, 29786, 23217, 10571, 10603, 8522, 10604, 10604, 19124, 14803, 14895, 12847, 17105, 12879, 10732, 6407, 2113, 2113, 8483, 6338, 4225, 4258, 4163, 8585, 15056, 19349, 21494, 38099, 33905, 34004, 33972, 4226, 27600, 23276, 33414, 20965, 10537, 4195, 33, 14858, 1, 12847, 34108, 40479, 42527, 42527, 46751, 53087, 46719, 38268, 12715, 21166, 31668, 25363, 29654, 31962, 40479, 40413, 42527, 42431, 40383, 42495, 44575, 42430, 36059, 27443, 25296, 18956, 8556, 25429, 14734, 25369, 16949, 19154, 14993, 23477, 21397, 15025, 8619, 2113, 4226, 4290, 4290, 4290, 6306, 4162, 10666, 19286, 23576, 21527, 10631, 38100, 29680, 33972, 36020, 10598, 14857, 25093, 22947, 8452, 16820, 2113, 2146, 34, 6374, 27769, 38334, 40446, 40414, 44671, 46719, 42494, 17072, 14795, 29652, 23282, 19056, 16976, 2217, 29849, 42559, 40447, 42495, 40415, 42495, 44639, 46655, 42300, 42168, 29458, 25263, 34075, 23285, 8461, 25305, 23287, 23380, 23413, 29850, 25624, 21397, 10734, 2213, 8452, 6435, 4290, 6403, 4162, 6279, 10674, 21368, 23576, 23608, 8583, 23341, 38100, 31761, 33939, 31793, 23308, 2113, 23013, 6274, 4195, 2150, 1, 6340, 2146, 21364, 32027, 38366, 40479, 44671, 44639, 34074, 8585, 23280, 25493, 19122, 17042, 2148, 8621, 14994, 44639, 46719, 40447, 42559, 40415, 42527, 40317, 38073, 16976, 33814, 25526, 40382, 25300, 25400, 25370, 29623, 23379, 25624, 31995, 29850, 23544, 14992, 4360, 2114, 6403, 6338, 6337, 6282, 4205, 14934, 19288, 23609, 21527, 6341, 4293, 29680, 38067, 33906, 31794, 21130, 31761, 8452, 16773, 6403, 4268, 4197, 33, 2081, 4195, 34140, 34173, 36286, 40447, 44607, 29815, 8488, 33879, 29687, 6445, 12749, 33, 19121, 10704, 42527, 46719, 44671, 40415, 40447, 42559, 40317, 14831, 34011, 40348, 36188, 33946, 31605, 35965, 25401, 35960, 25494, 31995, 34108, 31963, 27770, 21365, 8587, 2114, 4290, 6370, 6307, 4200, 8434, 12822, 21433, 23609, 23608, 8519, 10600, 6342, 33873, 35954, 31826, 29713, 6404, 29648, 8451, 20966, 8483, 10511, 68, 2148, 1, 2114, 31994, 36221, 38302, 40446, 23410, 21233, 33945, 31832, 34043, 4293, 4294, 17041, 10704, 40414, 44639, 42527, 40382, 36189, 42463, 33913, 42463, 42462, 44574, 40349, 29559, 29625, 31740, 35931, 40153, 27705, 42559, 42559, 34076, 34075, 25590, 10701, 2116, 8516, 6338, 2117, 10507, 8435, 12788, 21400, 23609, 21528, 8486, 8487, 6374, 6341, 35986, 33873, 33906, 31858, 4291, 19083, 10500, 10434, 8419, 10543, 4233, 2147, 0, 33, 23444, 32027, 34140, 4361, 29750, 36090, 31799, 29818, 4327, 17008, 21237, 21366, 42527, 46687, 42527, 36125, 33979, 38237, 40317, 42463, 40413, 44574, 40220, 23252, 38142, 31612, 40219, 38105, 34076, 42591, 42527, 40381, 36123, 25526, 10669, 10544, 10518, 4198, 14703, 4267, 10483, 14933, 19352, 23641, 23640, 8453, 12744, 6406, 6374, 6373, 35954, 29712, 31794, 33906, 14856, 6339, 6339, 10466, 8451, 23160, 4199, 2146, 2116, 4229, 35, 31930, 21299, 27573, 38203, 29719, 16944, 6508, 23413, 27704, 42526, 42527, 44607, 40382, 38238, 31898, 33913, 36124, 42430, 40381, 40349, 29558, 29626, 29562, 40254, 42396, 38204, 40446, 44671, 44607, 40349, 40218, 21300, 4296, 4334, 6440, 4295, 8461, 6315, 10515, 14934, 21400, 25721, 23640, 12712, 10631, 8551, 6406, 6438, 8486, 33906, 29680, 31793, 29680, 23374, 10533, 8419, 10467, 8419, 12623, 8397, 8363, 2149, 6312, 4166, 2, 23412, 36090, 33945, 29751, 23478, 36221, 38333, 40415, 42527, 46687, 46719, 38237, 33914, 25362, 31799, 40316, 38202, 35991, 23320, 25498, 38237, 42429, 38300, 40413, 42527, 44639, 40414, 42397, 42331, 14992, 2147, 8589, 4263, 6379, 4266, 12624, 10577, 12790, 21432, 25688, 25721, 6405, 4292, 2179, 8550, 6373, 6374, 6372, 33905, 23373, 29713, 19050, 29680, 21195, 23211, 6306, 4225, 4161, 6274, 4258, 2113, 6307, 6310, 4262, 35, 36122, 36187, 36253, 42559, 46783, 44607, 46687, 44541, 46687, 40286, 31834, 27443, 25263, 36057, 31700, 10636, 38333, 38333, 38333, 38333, 40381, 42526, 40446, 42527, 42462, 40316, 33976, 10733, 10601, 6507, 2118, 10542, 14704, 6347, 12597, 12846, 21428, 27833, 23672, 8550, 12711, 4260, 6340, 6437, 6374, 6374, 12712, 27436, 19115, 29681, 6340, 21293, 23276, 23211, 14758, 8419, 4193, 2112, 6339, 4225, 32, 6339, 4226, 2113, 2148, 40447, 40479, 34140, 42559, 42462, 46655, 44511, 40383, 38108, 33717, 23182, 33975, 31699, 23445, 36253, 38365, 40413, 40412, 38332, 42494, 42493, 40413, 40348, 40315, 19217, 17034, 8530, 6476, 18868, 8397, 10444, 8419, 10501, 19090, 25561, 29882, 25721, 6341, 4293, 6405, 4292, 6373, 8486, 6374, 4261, 10597, 23177, 21228, 31761, 6404, 8517, 23211, 23211, 23211, 8419, 6339, 6306, 4225, 6339, 6338, 2112, 6307, 4226, 4162, 38301, 40382, 40415, 40383, 42463, 44511, 40318, 38140, 35895, 21070, 14960, 27703, 25590, 29816, 36155, 38267, 40380, 38299, 38267, 38234, 36121, 27702, 8551, 27566, 6436, 8532, 18968, 10575, 10533, 10499, 14732, 12599, 21177, 33912, 34074, 25753, 8454, 4260, 4228, 4227, 4293, 4325, 6372, 4292, 4227, 14758, 23177, 25486, 29745, 16969, 4258, 23178, 21098, 19050, 14857, 6372, 6339, 4258, 6339, 4225, 6338, 4228, 2116, 4261, 4293, 38301, 40414, 40351, 42431, 40253, 38171, 33847, 29587, 33944, 36057, 36024, 36056, 35992, 36089, 36089, 36153, 34041, 27702, 6470, 6371, 25453, 2211, 6403, 12710, 10467, 10535, 12623, 18864, 35984, 54909, 33815, 42365, 29882, 27769, 6373, 2180, 2179, 4161, 2081, 4260, 4292, 4324, 4259, 4259, 14790, 21064, 25454, 27535, 25453, 18985, 21130, 16937, 8551, 4259, 6372, 48729, 10630, 6339, 6307, 6306, 12586, 4198, 4164, 3, 2116, 38202, 38203, 38171, 36026, 33913, 36057, 33944, 36025, 36024, 33910, 33910, 33910, 31797, 10632, 2210, 4259, 6436, 8517, 17131, 31856, 10612, 8464, 21075, 46547, 33772, 50740, 35864, 20985, 23290, 25559, 29882, 29882, 2179, 4325, 2113, 6275, 4226, 32, 4194, 4259, 4259, 4227, 4195, 16871, 16903, 25487, 17002, 25454, 21130, 10663, 6438, 33, 65, 4226, 52987, 59261, 57213, 48762, 19114, 10597, 6372, 8422, 4229, 4198, 12619, 8454, 10630, 21261, 40312, 38168, 38167, 42425, 50907, 55133, 10694, 4291, 4291, 6339, 38066, 4226, 4258, 12750, 55066, 50709, 37998, 42259, 23091, 14669, 8454, 8455, 8427, 19094, 27641, 31930, 29849, 2113, 4193, 4193, 4193, 2113, 2081, 32, 2146, 4226, 4259, 6340, 4259, 16904, 12711, 23406, 4259, 12809, 6470, 4291, 33, 33, 0, 6371, 57149, 57181, 55133, 59261, 59228, 57180, 59261, 57213, 59261, 59326, 59293, 59358, 59293, 57213, 59358, 55100, 57213, 55101, 55101, 52988, 46615, 8419, 8419, 10563, 6308, 6403, 14772, 16821, 12620, 10568, 10569, 10543, 12658, 14714, 16827, 12698, 21209, 21397, 31962, 31962, 4193, 4193, 4226, 2113, 2081, 2081, 2113, 32, 4194, 4291, 4259, 2146, 2114, 10630, 12841, 23342, 2211, 98, 2113, 2113, 0, 2145, 2081, 40244, 57181, 55133, 57213, 59260, 57115, 59326, 59293, 59293, 59293, 59261, 59326, 57213, 59358, 59327, 57213, 55100, 57246, 57213, 55165, 53020, 21326, 8614, 8496, 16917, 12691, 16852, 14771, 14739, 10578, 14771, 16884, 16794, 14747, 14746, 14778, 17012, 23541, 31994, 31994, 6274, 4194, 2113, 2113, 2113, 4161, 2113, 2145, 2113, 4259, 4259, 2146, 2082, 2082, 17003, 19180, 19180, 4259, 2113, 2080, 0, 2179, 2113, 2113, 50842, 57213, 55133, 59326, 57115, 59261, 59325, 59293, 59325, 59293, 59293, 59293, 59294, 59294, 57246, 52987, 57213, 57213, 55133, 55101, 36182, 29844, 23537, 19247, 31924, 4323, 2145, 4226, 6371, 6403, 6343, 10536, 8392, 12649, 10537, 14925, 23509, 34107, 32026, 4193, 4161, 2113, 2113, 2081, 2146, 2145, 2113, 2113, 2113, 4227, 2114, 2146, 2114, 4260, 19147, 17035, 2113, 2113, 0, 4259, 4226, 2081, 2081, 2113, 52922, 57181, 57181, 59261, 59228, 59293, 59326, 59261, 59326, 59326, 59326, 59293, 59326, 57213, 57213, 53019, 57246, 55165, 57213, 53020, 46715, 27764, 23506, 29909, 23538, 21521, 29778, 14891, 21295, 25651, 12808, 8419, 6305, 14693, 12908, 36122, 36220, 34107, 4161, 2113, 4161, 2112, 4193, 4193, 2113, 2112, 2113, 2114, 2179, 2114, 2146, 2146, 66, 6437, 2113, 2081, 0, 4227, 4259, 2145, 2081, 2081, 2081, 19114, 52987, 55067, 57180, 59228, 59228, 59293, 59261, 59293, 59293, 59294, 59326, 59261, 59326, 59294, 55068, 55100, 55133, 55133, 53053, 57213, 31989, 27731, 29876, 21425, 25651, 31990, 29877, 19279, 27796, 29909, 65, 6371, 6371, 21165, 29815, 34139, 36155, 4161, 4161, 4161, 4161, 2146, 4161, 2113, 2081, 4161, 2146, 2114, 2146, 2114, 2146, 4259, 2081, 2113, 33, 33, 2178, 65, 2081, 2113, 2081, 2113, 2113, 48760, 55068, 55100, 57212, 59228, 59293, 59293, 57245, 59326, 59326, 57245, 59261, 59294, 59294, 57245, 59293, 59326, 57213, 50907, 55133, 40408, 21425, 23538, 25683, 31957, 21457, 23570, 21425, 23537, 25683, 8681, 2113, 6404, 17070, 29880, 34106, 34075, 2080, 2113, 2145, 2081, 2113, 2113, 2113, 4161, 6405, 2114, 2146, 2147, 6340, 2179, 2146, 2081, 33, 12776, 17002, 14922, 2081, 2113, 2113, 2113, 2113, 2081, 2113, 52986, 57245, 55068, 59293, 57245, 57213, 57213, 57213, 57245, 57246, 59294, 59294, 59359, 59262, 59261, 57116, 59261, 57181, 53020, 38263, 19312, 31957, 21425, 23505, 34102, 31990, 27828, 23570, 23505, 21424, 14922, 4227, 17168, 29913, 34139, 34074]
cur = 0
lcd.erase()
for col in range(0,140,2):
    for row in range(0,125,2):
        if cur < len(csv):
            lcd.set_pixel(col, row, csv[cur])
            lcd.set_pixel(col+1, row, csv[cur])
            lcd.set_pixel(col, row+1, csv[cur])
            lcd.set_pixel(col+1, row+1, csv[cur])
            cur += 1

for i in range(lcd.h):
    lcd.set_pixel(120, i, 65535)

for i in range(lcd.h):
    lcd.set_pixel(94, i, 65535)

for i in range(lcd.w):
    lcd.set_pixel(i, 155, 65535)

for i in range(lcd.w):
    lcd.set_pixel(i, 126, 65535)

n_li = [(21,135),(20,134),(19,133),(18,133),(17,133),(16,133),(15,133),(14,134),(13,135),(13,136),(13,137),(13,138),(14,139),(15,140),(16,140),(17,140),(18,140),(19,140),(20,141),(21,142),(21,143),(21,144),(21,145),(20,146),(19,147),(18,147),(17,147),(16,147),(15,147),(14,146),(13,145),    (28,147),(28,146),(29,145),(29,144),(30,143),(30,142),(31,141),(31,140),(32,139),(32,138),(33,137),(33,136),(34,135),(34,134),(40,147),(40,146),(39,145),(39,144),(38,143),(38,142),(37,141),(37,140),(36,139),(36,138),(35,137),(35,136),(34,135),(34,134),(36,141),(35,141),(34,141),(33,141),(32,141),       (47,134),(47,135),(47,136),(47,137),(47,138),(47,139),(47,140),(47,140),(47,141),(47,142),(47,143),(47,144),(47,145),(47,146),(47,147),(48,141),(49,142),(50,143),(51,144),(52,145),(53,146),(54,147),(48,134),(49,134),(50,134),(51,134),(52,135),(53,136),(53,137),(53,138),(52,139),(51,140),(50,140),(49,140),(48,140),       (64,147),(64,146),(65,145),(65,144),(66,143),(66,142),(67,141),(67,140),(68,139),(68,138),(69,137),(69,136),(70,135),(70,134),(40,147),(76,147),(76,146),(75,145),(75,144),(74,143),(74,142),(73,141),(73,140),(72,139),(72,138),(71,137),(71,136),(70,135),(70,134),(72,141),(71,141),(70,141),(69,141),(68,141),(67,141)]

for x,y in n_li:
    lcd.set_pixel(x,y,65535)