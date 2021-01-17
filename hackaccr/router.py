from apihacka.viewsets import UsuarioViewset, CursoViewset, AulaViewset, Usuario_AulaViewset, UsuarioLeituraViewset, CursoLeituraViewset, LoginViewset, Usuario_AulaLeituraViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('usuario', UsuarioViewset)
router.register('curso', CursoViewset)
router.register('aula', AulaViewset)
router.register('usuarioaula', Usuario_AulaViewset)
router.register('usuarioleitura', UsuarioLeituraViewset)
router.register('cursoleitura', CursoLeituraViewset)
router.register('login', LoginViewset)
router.register('usuarioaulaleitura', Usuario_AulaLeituraViewset)


