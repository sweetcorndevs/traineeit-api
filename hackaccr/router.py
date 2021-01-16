from apihacka.viewsets import UsuarioViewset, CursoViewset, Usuario_CursoViewset, AulaViewset, Usuario_AulaViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('usuario', UsuarioViewset)
router.register('curso', CursoViewset)
router.register('usuariocurso', Usuario_CursoViewset)
router.register('aula', AulaViewset)
router.register('usuarioaula', Usuario_AulaViewset)

