class Priority:
    def __init__(self, title, category, action, status, importance, link):
        self.title = title
        self.category = category
        self.action = action
        self.status = status
        self.importance = importance
        self.link = link
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title
        
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        self._category = category
        
    @property
    def action(self):
        return self._action
    
    @action.setter
    def action(self, action):
        self._action = action
        
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, status):
        self._status = status
        
    @property
    def importance(self):
        return self._importance
    
    @importance.setter
    def importance(self, importance):
        self._importance = importance
        
    @property
    def link(self):
        return self._link
    
    @link.setter
    def link(self, link):
        self._link = link    