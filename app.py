#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from waitress import serve
from example import app

if __name__ == '__main__':
    serve(app.server, host='0.0.0.0', port=8050)


# In[ ]:



