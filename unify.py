import util

def unify(x, y, theta):
   if theta is False:
      return False
   if x == y:        
      return theta
   if util.is_variable(x):
      return unify_var(x, y, theta)
   if util.is_variable(y):
      return unify_var(y, x, theta)
   if util.is_compound(x) and util.is_compound(y):
      return unify(x.get_args(), y.get_args(), unify(x.get_op(), y.get_op(), theta))
   if util.is_list(x) and util.is_list(y) and len(x) == len(y):
      return unify(x[1:], y[1:], unify(x[0], y[0], theta))
   return False

def unify_var(var, x, theta): 
   if theta.contains(var):
      return unify(theta.get_substitute(var), x, theta)
   if theta.contains(x):
      return unify(var, theta.get_substitute(x), theta)
   theta.bind(var, x)
   return theta