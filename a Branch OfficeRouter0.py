System Bootstrap, Version 12.1(3r)T2, RELEASE SOFTWARE (fc1)
Copyright (c) 2000 by cisco Systems, Inc.
PT 1001 (PTSC2005) processor (revision 0x200) with 60416K/5120K bytes of memory

Readonly ROMMON initialized

Self decompressing the image :
########################################################################## [OK]

              Restricted Rights Legend

Use, duplication, or disclosure by the Government is
subject to restrictions as set forth in subparagraph
(c) of the Commercial Computer Software - Restricted
Rights clause at FAR sec. 52.227-19 and subparagraph
(c) (1) (ii) of the Rights in Technical Data and Computer
Software clause at DFARS sec. 252.227-7013.

           cisco Systems, Inc.
           170 West Tasman Drive
           San Jose, California 95134-1706



Cisco Internetwork Operating System Software
IOS (tm) PT1000 Software (PT1000-I-M), Version 12.2(28), RELEASE SOFTWARE (fc5)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2005 by cisco Systems, Inc.
Compiled Wed 27-Apr-04 19:01 by miwang

PT 1001 (PTSC2005) processor (revision 0x200) with 60416K/5120K bytes of memory
.
Processor board ID PT0123 (0123)
PT2005 processor: part number 0, mask 01
Bridging software.
X.25 software, Version 3.0.0.
4 FastEthernet/IEEE 802.3 interface(s)
2 Low-speed serial(sync/async) network interface(s)
32K bytes of non-volatile configuration memory.
63488K bytes of ATA CompactFlash (Read/Write)


         --- System Configuration Dialog ---

Continue with configuration dialog? [yes/no]: n


Press RETURN to get started!



Router>enable
Router#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#interface Serial2/0
Router(config-if)#no ip address
Router(config-if)#ip address 172.16.0.1 255.255.0.0
Router(config-if)#ip address 172.16.0.1 255.255.255.252
Router(config-if)#
Router(config-if)#exit
Router(config)#interface FastEthernet0/0
Router(config-if)#ip address 192.168.10.1 255.255.255.0
Router(config-if)#exit
Router(config)#hostname Router0
Router0(config)#
Router0(config)#interface FastEthernet0/0
Router0(config-if)#
Router0(config-if)#exit
Router0(config)#interface Serial2/0
Router0(config-if)#exit
Router0(config)#interface FastEthernet0/0
Router0(config-if)#ip address 192.168.10.1 255.255.255.0
Router0(config-if)#no shutdown

Router0(config-if)#
%LINK-5-CHANGED: Interface FastEthernet0/0, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/0, changed state to up

Router0(config-if)#exit
Router0(config)#in
Router0(config)#interface serial 0/0
%Invalid interface type and number
Router0(config)#interface Serial 0/0
%Invalid interface type and number
Router0(config)#interface Serial0/0
%Invalid interface type and number
Router0(config)#interface Serial0/0/0
                                  ^
% Invalid input detected at '^' marker.
	
Router0(config)#interface Serial2/0
Router0(config-if)#ip address 172.16.0.1 255.255.255.252
Router0(config-if)#no shutdown
HQ-R1(config-if)#no shutdown
HQ-R1(config-if)#router rip
HQ-R1(config-router)#network 192.168.10.0
HQ-R1(config-router)#network 172.16.0.0
HQ-R1(config-router)#exit
HQ-R1(config)#exit
HQ-R1#
%SYS-5-CONFIG_I: Configured from console by console
%LINK-5-CHANGED: Interface Serial2/0, changed state to down
Router0(config-if)#ip route 192.168.20.2 255.255.255.0 172.16.0.2
%Inconsistent address and mask
Router0(config)#ip route 192.168.20.0 255.255.255.0 172.16.0.2
Router0(config)#copy r
Router0(config)#copy runin
Router0(config)#exit
Router0#
%SYS-5-CONFIG_I: Configured from console by console

Router0#copy ru
Router0#copy running-config st
Router0#copy running-config startup-config 
Destination filename [startup-config]? 
Building configuration...
[OK]
Router0#
%LINK-5-CHANGED: Interface Serial2/0, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface Serial2/0, changed state to up

Router0#show ip route
Codes: C - connected, S - static, I - IGRP, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
       * - candidate default, U - per-user static route, o - ODR
       P - periodic downloaded static route

Gateway of last resort is not set

     172.16.0.0/30 is subnetted, 1 subnets
C       172.16.0.0 is directly connected, Serial2/0
C    192.168.10.0/24 is directly connected, FastEthernet0/0
S    192.168.20.0/24 [1/0] via 172.16.0.2
Router0#co
Router0#configure
Configuring from terminal, memory, or network [terminal]? 
Enter configuration commands, one per line.  End with CNTL/Z.
Router0(config)#router rip
Router0(config-router)#
Router0#
%SYS-5-CONFIG_I: Configured from console by console
