#### En el modelo Torneo.

[] Crear manager personalizados (torneos nuevos, en curso, finalizados y todos).
[] En el apartado registro de cada torneo si el torneo organiza delegación mostrar lista de registrados.
[] Tabla en la base de datos (otro model) solo para los torneos del circuito de verano.
[x] Formulario de registro en un torneo y guardar los datos en la db (formulario ModelForm).
[x] Añadir fecha límite inscripción en cada torneo y a partir de esta fecha calcular torneos nuevos, en curso,
   finalizados.
[x] Campo inscritos del modelo Torneo cambiar a un textarea.
[x] Fecha de publicación sin blank y sin null.
[x] Crear Breadcrumb en página torneo detail.
[x] FullCalendar enlace a la página detail del evento (torneo).
[x] Los estados en e Html la primera letra en mayúsculas (hay un filter tag en django para esto).
[x] Agregar "Delegación Malagueña de Ajedrez", al header junto a logo y quitar formulario buscar
[x] Mostrar las fechas de los torneos por orden ascendente
[x] Enlace opcional al sitio web que anuncia el torneo para que se puedan registrar, si el torneo lo realiza la
   federación Y EL TORNEO ES NUEVO entonces mostrar nuestro formulario de registro. Es decir si campo torneo.registrase
   esta vacío(false) y torne.estado es nuevo.
[x] Los estados, new, finished y progress, ponerlos en español.
[x] Mostrar las fechas en el html en el formato 'dd-mm-yy'
    Referencia: https://docs.djangoproject.com/en/4.0/ref/templates/builtins/#date
[x] Hacer responsive las tablas de datatables.


#### Algo nuevo y muy guay.
Line Breaks in the CSS Content Property
Referencia: https://www.digitalocean.com/community/tutorials/css-line-break-content-property
The CSS content property is very useful for generated content in the ::before or ::after speudo-elements.
To insert a new line / line break in that content, use the \A escape characters:

```
article h2::before {
  content: "Killing \A Me \A Softly";
  white-space: pre-wrap;
}
```