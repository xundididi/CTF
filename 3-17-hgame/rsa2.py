#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gmpy2,time

n=20009825321190817147963347442051848645000336424386939346276080303892938830978468883865096939010369211164496889554066362250659588656220842298166858655661318127372829597289087967547380136236626386470544343488308698913083828327292168712942475361870205910005035784342397506041791253029844494366387369699503134262891657189794050207749021028042635934918483017590572519580475948828187908443010713579723232915388260644322050961965307559877185043552130449517605233267873185739089790172109615861449171354606776131859765582549508046458007187356147775319574096663927646674967596503275755780154113292912277977650441567509457140143
e=2
c=11276768387639406169997533231062879430250136462512305127468735804849144724322098825651714250497166921684637563615970313478015998022841728073463694100833054875547140603479102218063033283024559033814543704665745305248197661146142121489172277735609441674723512858942001843838519086085091246645803803954875859233140684712680996684763144909422624752609564963732987239868247045418557656861860399004635444939531315079261663096466536784791883115937389245561776662381289412756713590876961018174315777429441413604654165274391861765190068056444464207139020429656290530404739547061849380150209984938360867220233189580698079032411
i=0
print ('n=', n)
print ('c=', c)

print ('[+]Detecting m...')
s=time.clock()

while 1:
	m, b = gmpy2.iroot(c + i * n, 2)
	if b:
		print ('  [-]m is: ' + '{:x}'.format(int(m)).decode('hex'))
		break
	print ('  [-]i = %d\r' % i)
	i = i+1
print ('[!]Timer:', round(time.clock() - s, 2), 's')