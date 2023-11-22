import pandas as pd

# Crear un DataFrame con los datos
data = {
    'PARCIALIDAD': ['0034-02', '0034-02', '0034-02', '0034-02', '0034-02'],
    'ESTATUS': ['APROBADO', 'APROBADO', 'APROBADO', 'APROBADO', 'APROBADO'],
    'CODIGO': ['PC-CJV-T1M-X-X-ELD-MR-0017-20230926'] * 5
}

df = pd.DataFrame(data)

# Crear un archivo XLSX con una hoja llamada "TOTAL"
nombre_archivo = 'C:\\Users\\hjorquera\\Desktop\\Minuta explicativa planimetria de repositorio\\PROCESO\\planillaPy.xlsx'
hoja = 'TOTAL'

with pd.ExcelWriter(nombre_archivo, engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name=hoja, index=False)

print(f'Se ha creado el archivo "{nombre_archivo}" con exito.')

