
/* WARNING: Function: __security_check_cookie replaced with injection: security_check_cookie */

uint FUN_009eb6b0(undefined4 *param_1)

{
  undefined4 *puVar1;
  char cVar2;
  byte bVar3;
  uint uVar4;
  uint uVar5;
  uint uVar6;
  byte local_110 [256];
  byte local_10 [4];
  byte local_c;
  byte local_b;
  byte local_a;
  byte local_9;
  uint local_8;
  
  local_8 = DAT_00bf93b4 ^ (uint)&stack0xfffffffc;
  if (param_1[4] == 9) {
    uVar6 = param_1[5];
    puVar1 = param_1;
    if (0xf < uVar6) {
      puVar1 = (undefined4 *)*param_1;
    }
    if (*(char *)(puVar1 + 1) == ' ') {
      memset(local_110,0xff,0x100);
      uVar4 = 0;
      do {
        local_110["ABCDEFGHJKLMNPQRSTWXYZ01234V6789"[uVar4]] = (byte)uVar4;
        uVar4 = uVar4 + 1;
      } while (uVar4 < 0x20);
      uVar4 = 0;
      do {
        if (uVar4 != 4) {
          uVar5 = uVar4 - 1;
          if (uVar4 < 5) {
            uVar5 = uVar4;
          }
          puVar1 = param_1;
          if (0xf < uVar6) {
            puVar1 = (undefined4 *)*param_1;
          }
          bVar3 = local_110[*(char *)((int)puVar1 + uVar4)];
          local_10[uVar5] = bVar3;
          if (bVar3 == 0xff) {
            return 0;
          }
        }
        uVar4 = uVar4 + 1;
      } while (uVar4 < 9);
      bVar3 = 0;
      uVar4 = (((((((uint)local_10[0] << 5 | (uint)local_10[1]) << 5 | (uint)local_10[2]) << 5 |
                 (uint)local_10[3]) << 5 | (uint)local_c) << 5 | (uint)local_b) << 2 |
              (uint)(local_a >> 3)) ^ 0xfef7ffd;
      for (uVar6 = uVar4; uVar6 != 0; uVar6 = uVar6 >> 5) {
        cVar2 = bVar3 + (char)uVar6;
        bVar3 = cVar2 * '\x02' - (cVar2 >> 7);
      }
      if (bVar3 == (byte)(local_a << 5 | local_9)) {
        return uVar4;
      }
    }
  }
  return 0;
}

