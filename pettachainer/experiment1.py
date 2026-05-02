# import os
# import sys
# import logging

# # --- PATH FIXER BLOCK ---
# # Change these paths if your folder structure is different
# PROJECT_ROOT = "/home/bek/Desktop/iCog/qwestor_PLN"
# PETTA_PATH = os.path.join(PROJECT_ROOT, "PeTTa")
# CHAINER_SOURCE = os.path.join(PROJECT_ROOT, "PeTTaChainer")

# # Ensure the local source is preferred over venv installed version
# if CHAINER_SOURCE not in sys.path:
#     sys.path.insert(0, CHAINER_SOURCE)

# # Set environment variable for PeTTa if it's not already set
# os.environ["PETTA_PATH"] = PETTA_PATH
# # ------------------------

from pettachainer import PeTTaChainer, check_query, check_stmt

  
# Create a handler instance  
handler = PeTTaChainer()  
  
# Add a statement to the knowledge base  
stmt_eval = handler.evaluate_statement("(: s1 (Dog fido) (STV 1.0 1.0))")  
check_stmt(stmt_eval)  
  
# Execute a query  
query_eval = handler.evaluate_query("(: $prf (Dog fido) $tv)")  
check_query(query_eval)
# You can print them to see:  
print(f"Statement valid: {check_stmt(stmt_eval)}")  # 1.0  
print(f"Query valid: {check_query(query_eval)}") 

