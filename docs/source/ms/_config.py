# docstyle-ignore
INSTALL_CONTENT = """
# Transformers pemasangan
! pip install transformers datasets
# 
Untuk memasang daripada sumber dan bukannya keluaran terakhir, ulas perintah di atas dan nyahkomen perintah berikut.
# ! pip install git+https://github.com/huggingface/transformers.git
"""

notebook_first_cells = [{"type": "code", "content": INSTALL_CONTENT}]
black_avoid_patterns = {
    "{processor_class}": "FakeProcessorClass",
    "{model_class}": "FakeModelClass",
    "{object_class}": "FakeObjectClass",
}
