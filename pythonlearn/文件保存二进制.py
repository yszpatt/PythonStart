#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-19 13:24:38
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import pickle
my_list = [123, 3.414, 'string', ['another', 'list']]
pickle.file = open('my_list.pkl', 'wb')
pickle.dump(my_list, pickle.file)
pickle.file.close()

pickle.file = open('my_list.pkl', 'rb')
my_list2 = pickle.load(pickle.file)
print(my_list2)
