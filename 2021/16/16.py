#!/usr/bin/env python3


from functools import reduce


def decode_literal(pstr):
    res = ''
    ind = 0
    while True:
        res += pstr[ind*5+1:(ind+1)*5]
        ind += 1
        if pstr[(ind-1)*5] == '0':
            break
    return int(res, 2), pstr[ind*5:]


def compute(tid, val):
    if tid == 0:
        return sum(val)
    elif tid == 1:
        return reduce(lambda x,y: x*y, val, 1)
    elif tid == 2:
        return min(val)
    elif tid == 3:
        return max(val)
    elif tid == 5:
        return 1 if val[0] > val[1] else 0
    elif tid == 6:
        return 1 if val[0] < val[1] else 0
    elif tid == 7:
        return 1 if val[0] == val[1] else 0
 

def decode(string):
    if len(string) < 8:
        return res, string
    
    ver = int(string[:3], 2)
    tid = int(string[3:6], 2)

    if tid == 4:
        val, string = decode_literal(string[6:])
        return ((ver, tid, val), string)

    operands = []
    # decoding based on the length of sub-packets
    if string[6] == '0':
        length = int(string[7:7+15], 2)
        string_inner = string[7+15:7+15+length]
        while len(string_inner) > 7:
            result, string_inner = decode(string_inner)
            operands += [result,]
        string = string[7+15+length:]
                
    # decoding based on the number of sub-packets
    else:
        cnt = int(string[7:7+11], 2)
        string = string[7+11:]
        for i in range(cnt):
            result, string = decode(string)
            operands += [result,]

    versions, _, values = [*zip(*operands)]
    val = compute(tid, values)
            
    return (ver + sum(versions), tid, val), string


def do_day16(packet):
    zeros = len(packet) - len(packet.lstrip('0'))
            
    packet = f'{int(packet, 16):b}'
    packet = '0'*(zeros*4) + '0'*((4-len(packet)%4)%4) + packet
    res, _ = decode(packet)

    print(res[0])
    print(res[2])


#packets = 'D2FE28'
#packets = '38006F45291200'
#packets = 'EE00D40C823060'

#packets = '8A004A801A8002F478' # 16
#packets = '620080001611562C8802118E34' # 12
#packets = 'C0015000016115A2E0802F182340' # 23
#packets = 'A0016C880162017C3686B18A3D4780' # 31

#packets = 'C200B40A82' # 1 + 2 --> 3
#packets = '04005AC33890' # 6 * 9 --> 54
#packets = '880086C3E88112' # min(7,8,9) --> 7
#packets = 'CE00C43D881120' # max(7,8,9) --> 9
#packets = 'D8005AC2A8F0' # 5 < 15 --> 1
#packets = 'F600BC2D8F' # 5 > 15 --> 0
#packets = '9C005AC2F8F0' # 5 == 15 --> 0
#packets = '9C0141080250320F1802104A08' # 1 + 3 == 2 * 2 --> 1

packets = '4057231006FF2D2E1AD8025275E4EB45A9ED518E5F1AB4363C60084953FB09E008725772E8ECAC312F0C18025400D34F732333DCC8FCEDF7CFE504802B4B00426E1A129B86846441840193007E3041483E4008541F8490D4C01A89B0DE17280472FE937C8E6ECD2F0D63B0379AC72FF8CBC9CC01F4CCBE49777098D4169DE4BF2869DE6DACC015F005C401989D0423F0002111723AC289DED3E64401004B084F074BBECE829803D3A0D3AD51BD001D586B2BEAFFE0F1CC80267F005E54D254C272950F00119264DA7E9A3E9FE6BB2C564F5376A49625534C01B0004222B41D8A80008446A8990880010A83518A12B01A48C0639A0178060059801C404F990128AE007801002803AB1801A0030A280184026AA8014C01C9B005CE0011AB00304800694BE2612E00A45C97CC3C7C4020A600433253F696A7E74B54DE46F395EC5E2009C9FF91689D6F3005AC0119AF4698E4E2713B2609C7E92F57D2CB1CE0600063925CFE736DE04625CC6A2B71050055793B4679F08CA725CDCA1F4792CCB566494D8F4C69808010494499E469C289BA7B9E2720152EC0130004320FC1D8420008647E8230726FDFED6E6A401564EBA6002FD3417350D7C28400C8C8600A5003EB22413BED673AB8EC95ED0CE5D480285C00372755E11CCFB164920070B40118DB1AE5901C0199DCD8D616CFA89009BF600880021304E0EC52100623A4648AB33EB51BCC017C0040E490A490A532F86016CA064E2B4939CEABC99F9009632FDE3AE00660200D4398CD120401F8C70DE2DB004A9296C662750663EC89C1006AF34B9A00BCFDBB4BBFCB5FBFF98980273B5BD37FCC4DF00354100762EC258C6000854158750A2072001F9338AC05A1E800535230DDE318597E61567D88C013A00C2A63D5843D80A958FBBBF5F46F2947F952D7003E5E1AC4A854400404A069802B25618E008667B7BAFEF24A9DD024F72DBAAFCB312002A9336C20CE84'
do_day16(packets)
