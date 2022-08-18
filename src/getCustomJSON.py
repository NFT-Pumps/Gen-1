import json

listOfCustoms = ["XMartian_Lamar_Jackson.jpg",
"XMartian_PC_Ssigned.jpg",
"xMartian_AirBorne.jpg",
"xMartian_Akeem.jpg",
"xMartian_AndrewForte.jpg",
"xMartian_Andy_Milonakis.jpg",
"xMartian_Anthony_Morrow.jpg",
"xMartian_BigBird.jpg",
"xMartian_Black_Excellence.jpg",
"xMartian_Brainiac.jpg",
"xMartian_Bsaic.jpg",
"xMartian_Captain_Booty_Signed.jpg",
"xMartian_Chief.jpg",
"xMartian_CoolJoe.jpg",
"xMartian_CryptoBully.jpg",
"xMartian_CryptoBully2.jpg",
"xMartian_CryptoCore.jpg",
"xMartian_CryptoCoreEuro.jpg",
"xMartian_CryptoCowboy_Signed.jpg",
"xMartian_CryptoGirl.jpg",
"xMartian_DFunch.jpg",
"xMartian_DaBaby.jpg",
"xMartian_Darcy_Donavan.jpg",
"xMartian_Darren.jpg",
"xMartian_DavidG.jpg",
"xMartian_DeFiBoy.jpg",
"xMartian_Dez.jpg",
"xMartian_Diablo.jpg",
"xMartian_Diablo_Signed.jpg",
"xMartian_Dom.jpg",
"xMartian_Drake.jpg",
"xMartian_Drill_Instructor.jpg",
"xMartian_Dutchess.jpg",
"xMartian_Enlighted.jpg",
"xMartian_FlavorsBSC.jpg",
"xMartian_FutureMattWallace.jpg",
"xMartian_Hangin.jpg",
"xMartian_ILove80s.jpg",
"xMartian_Intergalactic.jpg",
"xMartian_James.jpg",
"xMartian_Jay_Williams.jpg",
"xMartian_Jess.jpg",
"xMartian_John_Harding.jpg",
"xMartian_LG.jpg",
"xMartian_Lil_Wayne.jpg",
"xMartian_LisaJo.jpg",
"xMartian_LordNFT.jpg",
"xMartian_Lords_NFT_Signed.jpg",
"xMartian_Lords_Wifey_Signed.jpg",
"xMartian_LouThaWriter_Signed.jpg",
"xMartian_Marlon_Humphrey.jpg",
"xMartian_Martin.jpg",
"xMartian_Martin_Lawerence.jpg",
"xMartian_MattNFTy.jpg",
"xMartian_MoSanu.jpg",
"xMartian_MoneyMac.jpg",
"xMartian_MoonMark.jpg",
"xMartian_MoonMatt.jpg",
"xMartian_Ms.K.jpg",
"xMartian_Mutiat.jpg",
"xMartian_ObeyLord.jpg",
"xMartian_Obi.jpg",
"xMartian_Original41.jpg",
"xMartian_PC2.jpg",
"xMartian_Papa_Signed.jpg",
"xMartian_Pink_LegoFrames.jpg",
"xMartian_Puff_Daddy.jpg",
"xMartian_RedSwag.jpg",
"xMartian_RickGrimm_signed.jpg",
"xMartian_Ricky_Williams.jpg",
"xMartian_Safepool.jpg",
"xMartian_Shiggy.jpg",
"xMartian_Skye.jpg",
"xMartian_SmokeOut.jpg",
"xMartian_Snoop_Dog.jpg",
"xMartian_Sophie.jpg",
"xMartian_SoulTrippas.jpg",
"xMartian_SpaceKitty.jpg",
"xMartian_SpacedOut.png",
"xMartian_Stealie.jpg",
"xMartian_Swag.jpg",
"xMartian_Swift.jpg",
"xMartian_Tech_Signed.jpg",
"xMartian_Tre_Songz.jpg",
"xMartian_Trevon_Diggs.jpg",
"xMartian_Tristan_Jass.jpg",
"xMartian_Uncle_Paulie.jpg",
"xMartian_VaultDeFiJenn.jpg",
"xMartian_Viking.jpg",
"xMartian_VonMiller.jpg",
"xMartian_Woods.jpg",
"xMartian_ZZZ.png",
"xMartian_original29.jpg"]

tempJSON = {
    "attributes": [
        {
            "trait_type": "Martian Type",
            "value": "Super Rare"
        }
    ],
    "description": "xMartian Collection One",
    "external_url": "https://xMartianNFT.com/1",
    "image": "https://gateway.pinata.cloud/ipfs/QmQ8R3mSV7kefGJmWJuRqNdLANTAzR6g2h7qedX3ai6uPg/",
    "name": "xMartian00001"
}

for customImg in listOfCustoms:
    tempJSON["name"] = customImg
    tempJSON["image"] = "https://gateway.pinata.cloud/ipfs/QmQ8R3mSV7kefGJmWJuRqNdLANTAzR6g2h7qedX3ai6uPg/" + tempJSON["name"],
    finalJSON = json.dumps(tempJSON, indent=4)
    with open('src/output/newJSON/' + tempJSON["name"] + '.json', 'w') as output_file:
        output_file.write(finalJSON) 